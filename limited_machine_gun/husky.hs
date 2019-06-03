runDFA :: Int -> String -> Bool

runDFA 684 (x:xs) = if x == 'd' then False else False
runDFA 493 (x:xs) = if x == 'r' then runDFA 683 xs else False
runDFA 96  (x:xs) | x == 'l' = runDFA 239 xs | x == 't' = runDFA 367 xs | otherwise = False
runDFA 143 (x:xs) = if x == 'e' then runDFA 30  xs else False
runDFA 420 (x:xs) = if x == 'd' then runDFA 393 xs else False
runDFA 59  (x:xs) = if x == 'a' then runDFA 493 xs else False
runDFA 455 (x:xs) = if x == 'i' then runDFA 171 xs else False
runDFA 92  (x:xs) = if x == 'm' then runDFA 127 xs else False
runDFA 393 (x:xs) = if x == '_' then runDFA 98  xs else False
runDFA 251 (x:xs) = if x == 'n' then runDFA 452 xs else False
runDFA 485 (x:xs) = if x == 'y' then False else False
runDFA 164 (x:xs) = if x == 'm' then runDFA 272 xs else False
runDFA 46  (x:xs) = if x == '_' then runDFA 109 xs else False
runDFA 61  (x:xs) = if x == 'p' then runDFA 455 xs else False
runDFA 174 (x:xs) = if x == 'r' then runDFA 301 xs else False
runDFA 476 (x:xs) = if x == 'n' then runDFA 334 xs else False
runDFA 432 (x:xs) | x == 'm' = runDFA 624 xs | otherwise = False
runDFA 180 (x:xs) = if x == 'e' then runDFA 396 xs else False
runDFA 209 (x:xs) = if x == 'm' then runDFA 176 xs else False
runDFA 159 (x:xs) = if x == '_' then runDFA 262 xs else False
runDFA 29  (x:xs) = if x == '_' then runDFA 61  xs else False
runDFA 35  (x:xs) = if x == 'd' then runDFA 363 xs else False
runDFA 228 (x:xs) = if x == 'f' then runDFA 174 xs else False
runDFA 13  (x:xs) = if x == 'p' then False else False
runDFA 751 (x:xs) = if x == 'e' then False else False
runDFA 414 (x:xs) = if x == '_' then runDFA 32  xs else False
runDFA 325 (x:xs) = if x == 'I' then runDFA 451 xs else False
runDFA 334 (x:xs) = if x == 'k' then runDFA 273 xs else False
runDFA 279 (x:xs) = if x == 'l' then runDFA 414 xs else False
runDFA 565 (x:xs) = if x == 'd' then runDFA 624 xs else False
runDFA 328 (x:xs) = if x == 'a' then runDFA 1337 xs else False
runDFA 176 (x:xs) = if x == '_' then runDFA 96  xs else False
runDFA 247 (x:xs) = if x == 'a' then runDFA 695 xs else False
runDFA 517 (x:xs) = if x == 'o' then runDFA 527 xs else False
runDFA 172 (x:xs) = if x == 'l' then runDFA 54  xs else False
runDFA 572 (x:xs) = if x == 'm' then runDFA 281 xs else False
runDFA 367 (x:xs) = if x == 'h' then runDFA 88  xs else False
runDFA 239 (x:xs) = if x == 'o' then runDFA 669 xs else False
runDFA 273 (x:xs) = if x == 's' then runDFA 222 xs else False
runDFA 222 (x:xs) | x == '_' = runDFA 325 xs | x == 'p' = runDFA 255 xs | otherwise = False
runDFA 255 (x:xs) = if x == 'b' then runDFA 729 xs else False
runDFA 729 (x:xs) = if x == 'c' then runDFA 383 xs else False
runDFA 383 (x:xs) = if x == 't' then runDFA 294 xs else False
runDFA 294 (x:xs) = if x == 'f' then False else False
runDFA 371 (x:xs) | x == 'h' = runDFA 83  xs | otherwise = False
runDFA 32  (x:xs) = if x == 'i' then runDFA 111 xs else False
runDFA 452 (x:xs) = if x == 'e' then runDFA 373 xs else False
runDFA 326 (x:xs) = if x == '_' then runDFA 679 xs else False
runDFA 1337 (x:xs) = if x == 'd' then True else False
runDFA 88  (x:xs) = if x == 'i' then runDFA 476 xs else False
runDFA 679 (x:xs) = if x == 'h' then runDFA 230 xs else False
runDFA 373 (x:xs) = if x == 'e' then runDFA 420 xs else False
runDFA 272 (x:xs) = if x == 'y' then runDFA 9   xs else False
runDFA 171 (x:xs) = if x == 'l' then runDFA 172 xs else False
runDFA 109 (x:xs) = if x == 's' then runDFA 517 xs else False
runDFA 451 (x:xs) = if x == '_' then runDFA 251 xs else False
runDFA 363 (x:xs) = if x == 'e' then runDFA 328 xs else False
runDFA 669 (x:xs) = if x == 'v' then runDFA 180 xs else False
runDFA 111 (x:xs) = if x == 's' then runDFA 46  xs else False
runDFA 141 (x:xs) = if x == 'k' then runDFA 143 xs else False
runDFA 30  (x:xs) = if x == 'l' then runDFA 279 xs else False
runDFA 668 (x:xs) | x == 't' = runDFA 323 xs | x == 'n' = runDFA 485 xs | otherwise = False
runDFA 83  (x:xs) | x == 'a' = runDFA 179 xs | x == 'e' = runDFA 187 xs | otherwise = False
runDFA 54  (x:xs) = if x == '_' then runDFA 228 xs else False
runDFA 28  (x:xs) = if x == 'h' then runDFA 59  xs else False
runDFA 283 (x:xs) = if x == 'h' then runDFA 312 xs else False
runDFA 230 (x:xs) = if x == 'e' then runDFA 577 xs else False
runDFA 72  (x:xs) = if x == 'h' then False else False
runDFA 9   (x:xs) | x == '_' = runDFA 371 xs | otherwise = False
runDFA 312 (x:xs) = if x == 'e' then runDFA 675 xs else False
runDFA 675 (x:xs) = if x == 'r' then False else False
runDFA 624 (x:xs) = if x == 'b' then runDFA 160 xs else False
runDFA 323 (x:xs) = if x == 'c' then runDFA 72  xs else False
runDFA 187 (x:xs) = if x == 'a' then runDFA 1337 xs else False
runDFA 18  (x:xs) = if x == 's' then runDFA 141 xs else False
runDFA 397 (x:xs) = if x == '_' then runDFA 703 xs else False
runDFA 160 (x:xs) = if x == 'a' then runDFA 1337 xs else False
runDFA 703 (x:xs) = if x == 'm' then runDFA 751 xs else False
runDFA 695 (x:xs) = if x == 't' then runDFA 283 xs else False
runDFA 527 (x:xs) = if x == '_' then runDFA 28  xs else False
runDFA 281 (x:xs) = if x == 'e' then runDFA 326 xs else False
runDFA 396 (x:xs) = if x == 's' then runDFA 397 xs else False
runDFA 0   (x:xs) = if x == 'm' then runDFA 134 xs else False
runDFA 179 (x:xs) = if x == 'a' then runDFA 18  xs else False
runDFA 308 (x:xs) = if x == 'o' then runDFA 209 xs else False
runDFA 577 (x:xs) = if x == 'l' then runDFA 13  xs else False
runDFA 301 (x:xs) = if x == 'o' then runDFA 92  xs else False
runDFA 436 (x:xs) = if x == 'o' then runDFA 572 xs else False
runDFA 262 (x:xs) | x == 'm' = runDFA 308 xs | x == 'f' = runDFA 247 xs | otherwise = False
runDFA 127 (x:xs) = if x == '_' then runDFA 164 xs else False
runDFA 134 (x:xs) | x == 'a' = runDFA 668 xs | x == 'y' = runDFA 159 xs | otherwise = False
runDFA 98  (x:xs) | x == 'a' = runDFA 29  xs | x == 's' = runDFA 436 xs | otherwise = False

parse :: String -> Bool
parse = runDFA 0

main = do
  print("Hello! Input right string to win: ")
  user_input <- getLine
  if parse user_input == True
      then print("Yeah, it was hard, congrats!")
      else print("No, no, no. Maybe it's not yours? Get a Husky and forget about the Haskell.")
