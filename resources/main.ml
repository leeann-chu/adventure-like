(** [game_play adv st] prints the description of the current room the
    user is in based on [st] and calls [error_play adv st] to continue
    the game.*)
    let rec game_play adv st =
      let curr_room = State.current_room_id st in
      print_string ("\n" ^ Adventure.description adv curr_room ^ "\n");
      error_play adv st
    
    (** [error_play adv st] plays the game. It calls [game_play adv st] if
        the user inputs a valid input and recurses if the user inputs an
        invalid input. When the user inputs 'quit,' [error_play adv st]
        returns. *)
    and error_play adv st =
      print_string "\n> ";
      try
        let command =
          match read_line () with
          | exception End_of_file -> Command.Quit
          | command -> Command.parse command
        in
        let exit =
          match command with
          | Command.Go exit -> String.concat " " exit
          | Command.Quit -> "quit"
        in
        if exit <> "quit" then
          let new_state =
            match State.go exit adv st with
            | State.Illegal ->
                print_string "\nYou cannot go there from here.\n";
                st
            | State.Legal new_state -> new_state
          in
          if st <> new_state then game_play adv new_state
          else error_play adv new_state
        else print_string "\nFarewell, friend.\n"
      with
      | Command.Empty ->
          print_string
            "\n\
             I don't understand. Please type 'go', followed by the name of \
             a place or direction, or 'quit' to exit the game.\n";
          error_play adv st
      | Command.Malformed ->
          print_string
            "\n\
             I don't understand. Please type 'go', followed by the name of \
             a place or direction, or 'quit' to exit the game.\n";
          error_play adv st
    
    (** [play_game f] starts the adventure in file [f]. *)
    let rec play_game f =
      if f = "quit" then print_string "\nfarewell, friend.\n"
      else
        try
          let json = Yojson.Basic.from_file f in
          let adv = Adventure.from_json json in
          let init_state = State.init_state adv in
          game_play adv init_state
        with Sys_error potential_error -> (
          print_string "\nInvalid file name.\n";
          print_string "\n> ";
          match read_line () with
          | exception End_of_file -> ()
          | file_name -> play_game file_name)
    
    (** [main ()] prompts for the game to play, then starts it. *)
    let main () =
      ANSITerminal.print_string [ ANSITerminal.red ]
        "\n\nWelcome to the 3110 Text Adventure Game engine.\n";
      print_endline
        "Please enter the name of the game file you want to load.\n";
      print_string "> ";
      match read_line () with
      | exception End_of_file -> ()
      | file_name -> play_game file_name
    
    (* Execute the game engine. *)
    let () = main ()
    