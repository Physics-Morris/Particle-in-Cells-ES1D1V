! --------------------------------------------------------------------
! MODULE  diagnosis
!
!    Modules:
!    (1) var                  - contain all simulation variables
!
!    Subroutines:
!    (1) output(step)         - data output
!    (2) progress(step)       - print simulation progress
!    (3) para                 - print simulation parameter on screen
!    (4) error                - error diagnosis
!
!    Functions:
!    (1) KE                   - calculate total kinetic energy
!    (2) PE                   - calculate total potential energy
!    (3) P                    - calulate total momentum of particles
! --------------------------------------------------------------------
module diagnosis
    use var
    implicit none

    contains

! --------------------------------------------------------------------
!   Purpose: data output at every dump timestep
! --------------------------------------------------------------------
        subroutine output(step)
            implicit none
            integer :: step
            character(len=30) :: fm1, fm2

            if (mod(step, dump) .eq. 0) then
                write(fm1, '(A, I0, A)') '(', NG, '1f30.20)'
                write(fm2, '(A, I0, A)') '(', NP, '1f30.20)'

                if (flag(1) == 1) then
                    open(10, file=trim(loc)//'r.dat', status='unknown', &
                         access='append')
                    write(10, fm2) r
                    close(10)
                end if

                if (flag(2) == 1) then
                    open(11, file=trim(loc)//'v.dat', status='unknown', &
                         access='append')
                    write(11, fm2) v
                    close(11)
                end if

                if (flag(3) == 1) then
                    open(12, file=trim(loc)//'rho.dat', status='unknown', &
                         access='append')
                    write(12, fm1) rho
                    close(12)
                end if

                if (flag(4) == 1) then
                    open(13, file=trim(loc)//'phi.dat', status='unknown', &
                         access='append')
                    write(13, fm1) phi
                    close(13)
                end if

                if (flag(5) == 1) then
                    open(14, file=trim(loc)//'E.dat', status='unknown', &
                         access='append')
                    write(14, fm1) E
                    close(14)
                end if

                if (flag(6) == 1) then
                    open(15, file=trim(loc)//'KE.dat', status='unknown', &
                         position="append")
                    write(15, '(2f30.20)') t, KE()
                    close(15)
                end if

                if (flag(6) == 1) then
                    open(16, file=trim(loc)//'PE.dat', status='unknown', &
                         position="append")
                    write(16, '(2f30.20)') t, PE()
                    close(16)
                end if

                if (flag(7) == 1) then
                    open(17, file=trim(loc)//'P.dat', status='unknown', &
                         position="append")
                    write(17, '(2f30.20)') t, P()
                    close(17)
                end if
            end if
        end subroutine output


! --------------------------------------------------------------------
!   Purpose: calculate kinetic energy of particle
! --------------------------------------------------------------------
        function KE()
            implicit none
            double precision :: KE
            integer :: i

            KE = 0.0d0
            do i = 1, NP
                KE = KE + ((v(i)+vp(i))/2.d0)**2
            end do
            KE = KE * .5d0 * L / DBLE(NP)
        end function KE


! --------------------------------------------------------------------
!   Purpose: calculate potential energy of particle
! --------------------------------------------------------------------
        function PE()
            implicit none
            double precision :: PE
            integer :: i

            PE = 0.d0
            do i = 1, NG
                PE = PE + E(i) * E(i)
            end do
            PE = PE * .5d0 * dx
        end function PE


! --------------------------------------------------------------------
!   Purpose: calculate momentum of particle
! --------------------------------------------------------------------
        function P()
            implicit none
            double precision :: P
            integer :: i

            P = 0.d0
            do i = 1, NP
                P = P + (v(i) + vp(i)) / 2.d0
            end do
            P = P * L / DBLE(NP)
        end function P

! --------------------------------------------------------------------
!   purpose: print simulation progress 
! --------------------------------------------------------------------
        subroutine progress(step)
            implicit none
            integer :: times, step

            if (mod(step, dump) .eq. 0) then
                times = nint(tmax/dt)
                write(6, '(a, 1f4.1, a2)') "left percentage:", &
                     (1.d0-t/tmax)*100.d0, '%'
            end if
        end subroutine progress


! --------------------------------------------------------------------
!   purpose: print simulation parameter on screen
! --------------------------------------------------------------------
        subroutine para
            implicit none
            integer :: i
            call execute_command_line('python3 name.py')
            ! print simulation parameter
            write(6, *) repeat('-', 40)
            write(6, '(A, f6.3)') 'dt:', dt
            write(6, *) repeat('-', 40)
            write(6, '(A, I6)') 'number of timestep:', nint(tmax/dt)
            write(6, *) repeat('-', 40)
            write(6, '(A, f8.2)') 'Length:', L
            write(6, *) repeat('-', 40)
            write(6, '(A, f6.3)') 'Cell Length:', CL
            write(6, *) repeat('-', 40)
            write(6, '(A, I6)') 'Particle per Cell:', PPC
            write(6, *) repeat('-', 40)
            write(6, '(A, I6)') 'Number of Grid:', NG
            write(6, *) repeat('-', 40)
            write(6, '(A, I6)') 'output timestep', dump
            write(6, *) repeat('-', 40)
            write(6, '(A, A)') 'Data will be store at: ', loc
            write(6, *) repeat('-', 40)
            write(6, *) 'Removeing file in the directory in...'
            ! count down
            do i = 5, 1, -1
                write(6, '(I3.1, A4)') i, 'sec'
                call sleep(1)
            end do
            ! delete all file in the directory
            call execute_command_line('rm '//trim(loc)//'*')
        end subroutine para


! --------------------------------------------------------------------
!   purpose: error diagnosis
! --------------------------------------------------------------------
        subroutine error
            implicit none
            integer :: i
            do i = 1, NP
                ! check particles are in the box
                if (abs(r(i)-L/2.d0) .gt. L/2.d0) then
                    print*, 'No.', i, 'particle out of simulation box'
                end if
            end do
        end subroutine error
end module diagnosis
