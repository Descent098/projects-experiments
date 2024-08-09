PROGRAM name
  IMPLICIT NONE
  CHARACTER(LEN=100) :: full_name

  ! Read the name from the user
  PRINT *, "Enter your name:"
  READ(*, '(A)') full_name

  ! Call the function to print the greeting
  CALL PrintHello(full_name)

CONTAINS

  SUBROUTINE PrintHello(fname)
    CHARACTER(LEN=*) :: fname
    PRINT *, "Hello ", TRIM(ADJUSTL(fname))
  END SUBROUTINE PrintHello

END PROGRAM name