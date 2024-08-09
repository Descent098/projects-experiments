-- Takes in a list of strings in and print them with their index
printShoppingList :: [String] -> IO ()
printShoppingList items =
    mapM_ putStrLn [show idx ++ ". " ++ item | (idx, item) <- zip [1..] items]


-- Example usage
main :: IO ()
main = do
    putStrLn "Shopping List"
    putStrLn "============="
    printShoppingList ["Eggs", "Ham", "Spam"]