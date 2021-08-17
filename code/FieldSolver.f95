! --------------------------------------------------------------------
! MODULE  FieldSolver
!
!    Modules:
!    (1) var                  - contain all simulation variables
!
!    Subroutines:
!    (1) density              - calculate electron density
!    (2) field                - calculate the electric field on the
!                               grid
!    (3) Poisson              - solving periodic Poisson equation
!    (4) Inverse              - finding inverse matrix
! --------------------------------------------------------------------
module FieldSolver
    use var 
    implicit none

    contains

! --------------------------------------------------------------------
!   purpose: calculate electron density
!
!   methods: first-oder particle weighting(cloud-in-cell)
! --------------------------------------------------------------------
        subroutine density
            implicit none
            double precision :: y
            integer :: i, j

            rho = 0.d0
            do i = 1, NP
                j = floor(r(i) / dx)
                y = r(i) / dx - dble(j)
                if ( j == 0 ) then
                    rho(NG) = rho(NG) + (1.d0 - y) / dx
                    rho(1) = rho(1) + y / dx
                else 
                    rho(j) = rho(j) + (1.d0 - y) / dx
                    rho(j+1) = rho(j+1) + y / dx
                end if
            end do
            ! normalize
            rho = rho / n0 - 1.d0
        end subroutine density


! --------------------------------------------------------------------
!   Purpose: Calculate the electric field on the grid
!
!   Methods: First-order force(NGP)
! --------------------------------------------------------------------
        subroutine field
            implicit none
            integer :: i

            E(1) = (phi(NG) - phi(2)) / 2.d0 / dx
            E(NG) = (phi(NG-1) - phi(1)) / 2.d0 / dx
            do i = 2, NG-1
                E(i) = (phi(i-1) - phi(i+1)) / 2.d0 / dx
            end do
        end subroutine field


! --------------------------------------------------------------------
!   Purpose: solving periodic Poisson equation phi(x)=phi(x+L)
! --------------------------------------------------------------------
        subroutine Poisson
            implicit none
            integer :: i

            ! let phi_NG=0
            phi(NG)=0.d0

            ! solve for phi_1
            phi(1)=0.d0
            do i = 1, NG
                phi(1) = phi(1) + dble(i) * rho(i)
            end do
            phi(1) = phi(1) / dble(NG)

            ! then solve for phi_2
            phi(2) = rho(1) + 2.d0 * phi(1) 

            ! solve for phi_3 to phi_{NG-1}
            do i = 3, NG-1
                phi(i) = rho(i-1) - phi(i-2) + 2.d0 * phi(i-1)
            end do

            phi = dx * dx * phi
        end subroutine Poisson
end module FieldSolver
