! --------------------------------------------------------------------
! MODULE  ParticleMover
!
!    Modules:
!    (1) var                  - contain all simulation variables
!
!    Subroutines:
!    (1) rk4                  - use Runge-Kutta to solve eq of motion
!    (2) leapfrog             - use leapfrog to solve eq of motion
!    (3) halfleap             - leapfrog move -1/2 step
!
!    Functions:
!    (1) accel(r)             - find accelaration on particle at 
!                               position r
! --------------------------------------------------------------------
module ParticleMover
    use var
    implicit none

    contains

! --------------------------------------------------------------------
!   Purpose: find accelaration on particle by calculating force
! --------------------------------------------------------------------
        function accel(x)
            implicit none
            double precision :: accel, y, x
            integer :: j

            j = floor(x / dx)
            y = x / dx - dble(j)

            if ( j .eq. 0 ) then
                accel = - (E(NG) * (1.d0 - y) + E(1) * y)
            else
                accel = - (E(j) * (1.d0 - y) + E(j+1) * y)
            end if
        end function accel


! --------------------------------------------------------------------
!   Purpose: use Runge-Kutta method to move particles
! --------------------------------------------------------------------
        subroutine rk4
            implicit none
            integer :: i
            double precision :: w(4, 2)

            do i = 1, NP
                w(1, 1) = dt * accel(r(i))
                w(1, 2) = dt * v(i)

                w(2, 1) = dt * accel(r(i)+.5d0*w(1, 2))
                w(2, 2) = dt * v(i) + .5d0 * w(1, 1)

                w(3, 1) = dt * accel(r(i)+.5d0*w(2, 2))
                w(3, 2) = dt * v(i) + .5d0 * w(2, 1)

                w(4, 1) = dt * accel(r(i)+w(3, 2))
                w(4, 2) = dt * v(i) + w(3, 1)

                v(i) = v(i) + (w(1, 1) + 2.0d0 * w(2, 1) + &
                               2.0d0 * w(3, 1) + w(4, 1)) / 6.0d0
                r(i) = r(i) + (w(1, 2) + 2.0d0 * w(2, 2) + &
                               2.0d0 * w(3, 2) + w(4, 2)) / 6.0d0

                ! periodic bd condition
                if ( r(i) < 0.0d0 ) then
                    r(i) = r(i) + L
                else if ( r(i) > L ) then
                    r(i) = r(i) - L
                end if
            end do
        end subroutine rk4


! --------------------------------------------------------------------
!   Purpose: use leapforg method to move particles
! --------------------------------------------------------------------
        subroutine leapfrog
            IMPLICIT NONE
            integer :: i

            ! store previous step
            vp = v
            do i = 1, NP 
                v(i) = v(i) + accel(r(i)) * dt
                r(i) = r(i) + v(i) * dt

                ! check if particles are inside 0 <= x <= L
                if ( r(i) .le. 0.d0 ) then
                    r(i) = r(i) + L
                else if ( r(i) .ge. L ) then
                    r(i) = r(i) - L
                end if
            end do
        end subroutine leapfrog


! --------------------------------------------------------------------
!   Purpose: Moving -1/2 step to apply leapfrog algorithm
! --------------------------------------------------------------------
        subroutine halfleap
            implicit none
            integer :: i

            do i = 1, NP 
                v(i) = v(i) - .5d0 * accel(r(i)) * dt
            end do
        end subroutine halfleap
end module ParticleMover
