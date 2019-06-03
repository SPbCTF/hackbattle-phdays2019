IDENTIFICATION DIVISION.
PROGRAM-ID. Security-storage.
SECURITY. supermegaultraushellnotpassspbctfoneloveseruritydesu

DATA DIVISION.
WORKING-STORAGE SECTION.
  01 SUBPRG.
	02 TMPABOUT PIC X(30).
    02 TMPCHOICE PIC X(1).
	02 TMPAGE PIC 99.
	02 TMPLOGIN PIC X(10).
	02 TMPPASSW PIC X(10).
  01 TMPABOUT2 REDEFINES SUBPRG PIC X(40).


  01 USER.
	02 LOGIN PIC X(10).
	02 PASSW PIC X(10).
  	02 AGE PIC 99.
  	02 VIP PIC 9 VALUE 0.
  	02 ABOUT PIC X(30).

  01 CHOICE PIC 9.
    88 ONE VALUE "1".
    88 TWO VALUE "2".
    88 THREE VALUE "3".
	88 FOUR VALUE "4".
	88 FIVE VALUE "5".
  	88 SECRET VALUE "9".
    88 QUIT VALUE "6".

PROCEDURE DIVISION.

  DISPLAY "###########################################"
  DISPLAY "# WELCOME TO THE SUPER SECURITY STORAGE!  #"
  DISPLAY "###########################################".

MENU-LAB.
  DISPLAY " "
  DISPLAY "1. Register."
  DISPLAY "2. Login."
  DISPLAY "3. View info."
  DISPLAY "4. Change info."
  DISPLAY "5. Open the storage."
  DISPLAY "6. Quit."
  DISPLAY "? " NO ADVANCING
  ACCEPT CHOICE

  IF QUIT
    GOBACK
  END-IF

  IF ONE
    PERFORM REGISTER
  ELSE
    IF TWO
      PERFORM LOGIN-SECTION
    ELSE
      IF THREE
        PERFORM VIEW-INFO
	  ELSE
	    IF FOUR
		  PERFORM CHANGE-INFO
		ELSE
		  IF FIVE
		    PERFORM OPEN-STORAGE
		  ELSE
		    IF SECRET
			  PERFORM SECRET-SECTION
		    END-IF
		  END-IF
	    END-IF
      END-IF
    END-IF
  END-IF

  GO TO MENU-LAB.

REGISTER.
  DISPLAY "Now you are not able to add a new user. But you can try 'test' with password 'test'.".

END-REGISTER.
  EXIT.

LOGIN-SECTION.
  DISPLAY "Enter your login: " NO ADVANCING
  ACCEPT TMPLOGIN
  DISPLAY "Enter your password: " NO ADVANCING
  ACCEPT TMPPASSW
  IF TMPLOGIN = "test" and TMPPASSW = "test"
    MOVE TMPLOGIN to LOGIN
	MOVE TMPPASSW to PASSW
	MOVE 0 to AGE
	MOVE 0 to VIP
	MOVE SPACE to ABOUT
  ELSE
    DISPLAY "Login or password are wrong!"
  END-IF.
END-LOGIN-SECTION.
  EXIT.

VIEW-INFO.
  IF NOT LOGIN = SPACE
    DISPLAY "Login: ", LOGIN
	DISPLAY "Age:   ", AGE
	DISPLAY "VIP:   ", VIP
	DISPLAY "About: ", ABOUT
  ELSE
    DISPLAY "You should login first."
  END-IF.
END-VIEW-INFO.
  EXIT.

CHANGE-INFO.
  IF NOT LOGIN = SPACE

	DISPLAY "Do you want to change your age? [Y/N]: " NO ADVANCING
	ACCEPT TMPCHOICE
	IF TMPCHOICE = "Y"
	  DISPLAY "Age? " NO ADVANCING
	  ACCEPT TMPAGE
	END-IF

	DISPLAY "Do you want to tell something about yourself? [Y/N]: " NO ADVANCING
	ACCEPT TMPCHOICE
	IF TMPCHOICE = "Y"
	  DISPLAY "Information about you? "
	  ACCEPT TMPABOUT
	ELSE
	  DISPLAY "Are you sure? [Y/N]: " NO ADVANCING
	  ACCEPT TMPCHOICE
	  IF TMPCHOICE = "N"
	    DISPLAY "Information about you? "
	    ACCEPT TMPABOUT2
	  END-IF
	END-IF

	DISPLAY "Do you want to change your login? [Y/N]: " NO ADVANCING
	ACCEPT TMPCHOICE
	IF TMPCHOICE = "Y"
	  DISPLAY "New login? "
	  ACCEPT TMPLOGIN
	  IF TMPLOGIN = "admin"
	    DISPLAY "No no no. Go away."
		MOVE SPACE to TMPLOGIN
	  END-IF
	END-IF

	MOVE TMPABOUT to ABOUT
	MOVE TMPAGE to AGE
	IF NOT TMPLOGIN = SPACE
	  MOVE TMPLOGIN to LOGIN
	END-IF

	DISPLAY "Successful!"
  ELSE
    DISPLAY "You should login first."
  END-IF.
END-CHANGE-INFO.
  EXIT.

OPEN-STORAGE.
  DISPLAY "Trying to open the storage...".
  IF LOGIN = "admin" AND VIP = 1
    CALL "system" USING "cat /root/storage/storage.txt"
  ELSE
    DISPLAY "You are not allowed!"
  END-IF.

END-OPEN-STORAGE.
  EXIT.

SECRET-SECTION.
  DISPLAY "Ooops. You should not see this message...".
  MOVE 1 TO VIP.

END-SECRET-SECTION.
  EXIT.
