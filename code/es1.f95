! --------------------------------------------------------------------
! program  Electostatic 1D PIC simulation:
!
!    Modules:
!    (1) var                  - contain all simulation variables
!    (2) FieldSolver          - solving field
!    (3) ParticleMover        - solving eq of motion
!    (4) diagnosis            - I/O and calculate physics quantity
!
!    Subroutines:
!    (1) density              - calculate electron density
!    (2) field                - calculate the electric field on the
!                               grid
!    (3) init                 - choice of initial condition
!    (4) output(step)         - data output
!    (5) progress(step)       - print simulation progress
!    (6) para                 - print simulation parameter on screen
!    (7) rk4                  - use Runge-Kutta to solve eq of motion
!    (8) leapfrog             - use leapfrog to solve eq of motion
!    (9) halfleap             - leapfrog move -1/2 step
!   (10) error                - error diagnosis
!   (11) Poisson              - solving periodic Poisson equation
!   (12) Inverse              - finding inverse matrix
!
!    Functions:
!    (1) KE                   - calculate total kinetic energy
!    (2) PE                   - calculate total potential energy
!    (3) P                    - calulate total momentum of particles
!    (4) accel(r)             - find accelaration on particle at 
!                               position r
! --------------------------------------------------------------------
program ES1
    use var
    use FieldSolver
    use ParticleMover
    use diagnosis
    implicit none
    integer :: step=0

    call para
    call init
    call density
    call poisson
    call field
    call halfleap
    do step = 1, nint(tmax / dt)
        call progress(step)
        call density
        call poisson
        call field
        call leapfrog
        call output(step)
        t = t + dt
    end do
end program ES1
