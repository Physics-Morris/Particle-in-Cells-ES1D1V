! --------------------------------------------------------------------
! MODULE  var: variable and initial condition
!
!    Subroutines:
!    (1) init                 - choice of initial condition
! --------------------------------------------------------------------
module var
    implicit none

    ! define what type of real are being used
    double precision, parameter :: pi = 4.d0*atan(1.d0)
    double precision, parameter :: twopi = 8.d0*atan(1.d0)

    !!!!!!!!!!!!!!!! sim parameters !!!!!!!!!!!!!!!!
    ! Domain between 0 <= x <= L (unit: Debye length)
    double precision, parameter :: L = twopi / 0.6124d0
    ! cell length
    double precision, parameter :: CL = .7d0
    ! particle per cell
    integer, parameter :: PPC = 10000
    ! Number of grid point
    integer, parameter :: NG = nint(L/CL)
    ! Number of particle
    integer, parameter :: NP = NG*PPC

    ! beam velocity
    double precision, parameter :: vb = 1.d0
    ! time step (unit: 1/plasma f)
    double precision, parameter :: dt = .1d0
    ! spatial resolution
    double precision, parameter :: dx = L / dble(NG)
    ! electron density
    double precision, parameter :: n0 = dble(NP) / L
    ! maximum simulation time
    double precision, parameter :: tmax = 100.d0
    ! dump time step
    integer, parameter :: dump = 2
    ! output flag for    (  r, v, rho, phi, E, energy, momentum)
    integer, parameter :: flag(7) = (/ 1, 1, 1, 1, 1, 1, 1 /) 
    ! data storing location
    character(len=30), parameter :: loc = '../data/0612/'
    !!!!!!!!!!!!!!!! sim parameters !!!!!!!!!!!!!!!!


    !!!!!!!!!!!!!!!! variables !!!!!!!!!!!!!!!!
    ! particle position
    double precision :: r(NP)
    ! particle velocity
    double precision :: v(NP)
    ! store previous step of velocity
    double precision :: vp(NP)
    ! charge density on grid
    double precision :: rho(NG)
    ! electric potential on grid
    double precision :: phi(NG)
    ! electric field on grid
    double precision :: E(NG)
    ! simulation time
    double precision :: t = 0.d0
    !!!!!!!!!!!!!!!! variables !!!!!!!!!!!!!!!!

    contains

! --------------------------------------------------------------------
!   Purpose: choice of initial condition
! --------------------------------------------------------------------
        subroutine init
            implicit none
            integer :: i
            ! double precision :: vmin, vmax, Vi, f, fmax, x, rd

            ! uniform random position of the electron
            call random_seed()
            call random_number(r)
            r = r * L

            ! two cold stream 
            do i = 1, NP/2; v(i) = vb; end do
            do i = NP/2+1, NP; v(i) = -vb; end do

            ! two warm stream (rejection method)
            ! do i = 1, NP
                ! do
                    ! fmax = .5d0 * (1.d0 + DEXP(-2.d0 * Vb * Vb))
                    ! vmin = - 5.d0 * Vb
                    ! vmax = + 5.d0 * Vb
                    ! call random_number(rd)
                    ! Vi = vmin + (vmax - vmin) * rd
                    ! f = .5d0 * (DEXP(-(Vi - Vb) * (Vi - Vb) / 2.d0) + &
                                ! DEXP(-(Vi + Vb) * (Vi + Vb) / 2.d0))
                    ! call random_number(rd)
                    ! x = fmax * rd
                    ! if (x < f) then
                        ! exit
                    ! end if
                ! end do
                ! v(i) = Vi
            ! end do
        end subroutine init
end module
