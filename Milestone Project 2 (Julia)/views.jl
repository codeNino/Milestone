module views
    include("./database.jl")
    include("./Auth.jl")
    using .database: usersDB
    using .Auth

    function login()
        println(" Welcome to Charis Bank..\n Please Enter your UserName and Password to proceed ")
        println(" Username  ==> ")
        name = readline()
        println("\n")
        println(" Password  ==> ")
        pwd = readline()
        
        authenticated = verify_userPWD(pwd, name)
        user_exists = verify_userID(name)

        while !user_exists || !authenticated
            println("INVALID LOGIN CREDENTIALS......\n")
            println("\n Please Enter  '1'  to Try again or Enter '2' to Register as a new user \n ==>  ")
            action = readline()
            if action !== "2"
                println(" Username  ==> ")
                global name = readline()
                println("\n")
                println(" Password  ==> ")
                global pwd = readline()
                if verify_userID(name) && verify_userPWD(pwd, name)
                    break
                end
            else
                return register_user()
            end
        end

        return transactions_view(name)

    function  register_user()

        println(" Please Fill the form below \n ")
        println(" Enter your UserName:   ")
        user_name = readline()
        println(" Enter your full name:   ")
        fullname = readline()
        println(" Enter your Email:   ")
        email = readline()
        println(" Enter your Password:   \n (Password must contain digits, special characters and be at least 9 characters long) ")
        passwd = readline()
        while ! occursin(r"[&$*%#@&]", passwd) || match(r"[0-9]", passwd) === nothing || length(passwd) < 9
            if ! occursin(r"[&$%*#@&]", passwd)
                printstyled(" Password must contain special characters!! \n "; color = :red)
                println(" Please enter your secret password \n  (Password must contain digits, special characters and be at least 9 characters long) \n ==> ")
                global passwd = readline()
            elseif match(r"[0-9]", passwd) === nothing
                printstyled(" Password must contain digits !! \n "; color = :red)
                println(" Please enter your secret password \n  (Password must contain digits, special characters and be at least 9 characters long) \n ==> ")
                global passwd = readline()
            elseif length(passwd) < 9
                printstyled(" Password must be at least 9 characters long !! \n "; color = :red)
                println(" Please enter your secret password \n  (Password must contain digits, special characters and be at least 9 characters long) \n ==> ")
                global passwd = readline()
            end

            if occursin(r"[&$*#@&]", passwd) && occursin(r"[0-9]", passwd) && length(passwd) >= 9
                println( "Your Password has been accepted! \n")
                break
            end
        end
        
        println(" Please Confirm your password:   \n ==>  ")
        confirmed_passwd = readline()

        while confirmed_passwd !== passwd
                printstyled("Password not matching!! "; color=:red)
                println(" Please Confirm your password:   ")
                global confirmed_passwd = readline()
                if confirmed_passwd === passwd
                    break
                end
            end

        println(" Enter your contact line:  ")
        contact = readline()
        
        usersDB[user_name] = Dict("name" => fullname, "email"=> email,
                                    "password"=> passwd, "contact"=> contact,
                                    "account_balance"=>0)

        println("User registered Successfully!!! ")

        return login()

    end



    function transactions_view(name)

        println(" Please select your desired action below \n")
        printstyled(" A: Instant Transfer           C:  Withdrawal \n B:  Airtime Recharge              D:  Check Balance \n   E:  Quit  \n ==>    "; color = :green)
        action = readline()

        while action !== "A" && action !== "B" && action !== "C" && action !== "D" && action !== "E"
            printstyled(" Invalid Request....."; color= :red)
            println(" Please select your desired action below \n")
            printstyled(" A: Instant Transfer           C:  Withdrawal \n B:  Airtime Recharge              D:  Check Balance \n   E: Quit \n ==>  "; color = :green)
            global action = readline()
            if action === "A"
                break
                return instant_tranfer_view(name)
            elseif  action === "B"
                break
                return Airtime_Recharge(name)
            elseif action === "C"
                break
                return make_withdrawal(name)
            elseif action === "D"
                break
                return check_balance(name)
            elseif action === "E"
                exit()
            end
        end
    end

    function instant_tranfer_view(username)
        
        printstyled(" Bank to transfer: \n A: FLEMMING BANK     D: HOGWARTS BANK \n B: WEST MIDLANDS BANK     E: OTHERS \n C: REVENANT BANK  \n ==>"; color = :green)
        Banks = Dict("A" => "FLEMMING BANK", "B" => "WEST MIDLANDS BANK", "C" => "REVENANT BANK",
                    "D" => "HOGWARTS BANK", "E" => Dict("A" => "VIOLET BANK", "B" => "SPARKLING BANK",
                     "C" => "ORANGE BANK",
                    "D" => "REVERE"))
    
        bank = readline()

        if bank !== "E"
            println(" DESTINATION ACCOUNT NUMBER: \n ==> ")
            acc = readline()
            while length(acc) !== 10 || tryparse(Int, acc) === nothing 
                printstyled( " INVALID ACCOUNT NUMBER....PLEASE CHECK AND TRY AGAIN \n  "; color = :red)
                println(" Enter account number ==>  ")
                global acc = readline()
                if length(acc) === 10 && tryparse(Int, acc) !== nothing 
                    break
                end
            end

            println("\n AMOUNT TO TRANSFER ==>   \n")
            amount = parse(Int64, readline())

            println(" Please Enter Password to continue: \n Password ==>")
            pwd3 = readline()

            transaction_auth(pwd3, username)

            usersDB[username]["account_balance"] -= amount 
        
            printstyled(" YOU TRANSFERED $amount TO USER $acc AT $bank  "; color = :blue)
            println(" Press 1 to perform another transaction or 2  to Quit.. \n")
            action = readline()
            if action !== 1 
                exit()

            else
                return transactions_view(username)
            end

        else
            printstyled(" SELECT BANK: \n A: VIOLET BANK        C: ORANGE BANK \n B: SPARKLING BANK        D: REVERE \n ==>"; color = :green)
            readline()
            println(" DESTINATION ACCOUNT NUMBER: \n ==> ")
            acc = readline()
            while length(acc) !== 10 || tryparse(Int, acc) === nothing
                printstyled( " INVALID ACCOUNT NUMBER....PLEASE CHECK AND TRY AGAIN \n  "; color = :red)
                println(" Enter account number ==>  ")
                global acc = readline()
                if length(acc)===10 && tryparse(Int, acc) !== nothing
                    break
                end
            end

            println("\n AMOUNT TO TRANSFER ==>   \n")
            amount = parse(Int64,readline())

            println(" Please Enter Password to continue: \n Password ==>")
            pwd3 = readline()

            transaction_auth(pwd3, username)
            usersDB[username]["account_balance"] -= amount 
            printstyled(" YOU TRANSFERED $amount TO USER $acc AT $bank  "; color = :blue)
            println(" Press 1 to perform another transaction or 2  to Quit.. \n")
            action = readline()
            if action !== 1 
                exit()

            else
                return transactions_view(username)
            end
        end    
        
    end

    function Airtime_Recharge(username)

        printstyled( " Service Provider: \n A: VERIZON    C: REVERE \n B: LOKI     D: MOCA  \n ==>"; color = :green)
    
        readline()
    
        println(" Enter phone number to recharge:   ")
        phone = readline()
    
        println(" Enter Amount to recharge")
        amount = parse(Int64, readline())

        while amount > usersDB[username]["account_balance"]
            println("Insufficient Funds....")
            println(" Please Enter '1' to Try again or '2' to Perform another Transaction or 'Q' to Quit ")
            println(" ===>  ")
            action = readline()
            if action !== "1" && action !== "2"
                exit()
            elseif action === "1"
                println(" Enter Amount to recharge")
                global amount = parse(Int64, readline())
                if amount <= usersDB[username]["account_balance"]
                    break
                end
            elseif action === "2"
                return transactions_view(username)
            end
        end

        println(" Please Enter Password to continue: \n Password ==>")
        pwd = readline()
        transaction_auth(pwd, username)
        usersDB[username]["account_balance"] -= amount 
        printstyled(" YOU RECHARGED USER $phone WITH $amount "; color = :blue)
        println(" Press 1 to perform another transaction or 2  to Quit.. \n")
        action = readline()
        if action !== 1 
            clear()
            exit()
        else
            return transactions_view(username)
        end
    end

    function account_view()

        accounts = Dict("A"=> "Savings",
                    "B"=> "Current",
                "C"=> "Fixed Deposit")

        printstyled(" Select account: "; color = :green)
        printstyled(" A: Savings          C: Fixed Deposit \n B: Current "; color = :green)
            
        account = readline()
        while account !== "A" && account !== "B" && account !== "C"
            printstyled(" Select account: "; color = :green)
            printstyled(" A: Savings          C: Fixed Deposit \n B: Current "; color = :green)
            global account = readline()
            if account === "A" || action === "B" || action === "C"
                break
            end
        end
    end

    function amount_to_withdraw_view()

        fund = Dict("A"=> 2000, "B"=> 5000, "C"=> 10000)
        println(" Select amount to withdraw: ")
        printstyled(" A:  2000      C: 10000 \n B: 5000     D: Other Amount \n ==>  "; color = :green)    
        option = readline()

        while option !== "A" && option !== "B" && option !== "C" && option !== "D"
            printstyled(" Invalid Request.....\n"; color = :red)
            println(" Select amount to withdraw:\n ")
            printstyled(" A:  2000      C: 10000 \n B: 5000     D: Other Amount \n ==>  "; color = :green)
            option = readline()
            if option === "A" || option === "B" || option === "C" || option === "D"
                break
            end
        end

        if option === "A" || option === "B" || option === "C"
            money = fund[option]
            return money

        elseif option === "D"
            println("Please Enter amount to withdraw (Not greater than 20 000)")
            println(" Amount:   ")
            money = parse(Int64,readline())
            while money > 20000
                println(" Limit Exceeded....")
                println(" Please Enter amount not greater than 20000 \n ==> ")
                global money = parse(Int64,readline())
                if money <= 20000
                    break
                end
            end
            return money
        end
    end

    function make_withdrawal(username)

        account_view()

        amount = amount_to_withdraw_view()

        while amount > usersDB[username]["account_balance"]
            println("Insufficient Funds....")
            println(" Please Enter '1' to Try again or '2' to Perform another Transaction or 'Q' to Quit ")
            println(" ===>  ")
            action = readline()
            if action !== "1" && action !== "2"
                exit()
            elseif action === "1"
                global amount = amount_to_withdraw_view()
                if amount <= usersDB[username]["account_balance"]
                    break
                end
            elseif action === "2"
                return transactions_view(username)
            end
        end

        println(" Please Enter Password to continue: \n Password ==>")
        pwd = readline()
        transaction_auth(pwd, username)
        usersDB[username]["account_balance"] = usersDB[username]["account_balance"] - amount

        printstyled(" $amount has been debited from your account.... "; color = :green)
        println(" Press any key to exit")
        readline()
        exit()
    end

    function check_balance(username)

        account_view()
        account_balance = usersDB[username]["account_balance"]
        printstyled(" Your Account Balance is #$account_balance "; color=:green)
        println(" Please Enter '1' to Perform another Transaction or 'Q' to Quit ")
        println(" ===>  ")
        action = readline()
        if action !== "1"
            exit()
        else
            return transactions_view(username)
        end
   
    end

    export register_user, transactions_view, instant_tranfer_view, check_balance
    export make_withdrawal,  Airtime_Recharge

end