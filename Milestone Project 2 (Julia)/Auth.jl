module Auth
    include("./database.jl")
    using .database: usersDB

    clear() = run(`cmd /c cls`)


    function transaction_auth(pwd, username)
        token = 3
        while pwd !== usersDB[username]["password"]

            println("Password Incorrect...\n You have $token attempt(s) left \n")
            println("Press 1 to Try Again or 2 to Quit\n ===>  ")
            action = readline()
            if action === "2"
                exit()
            else
                println(" Please Enter your Secret Password \n ==>  ")
                global token -= 1
                global pwd = readline()
                if token === 0
                    printstyled(" Service Suspended "; color = :red)
                    clear()
                    exit()
                end
                if pwd === usersDB[username]["password"]
                    println("Transaction Authenticated")
                    break
                end
            end
        end
    end

    function verify_userID(username)

        if !haskey(usersDB, username)
            return false
        else
            return true
        end
    end


    function verify_userPWD(pwd, username)

        if pwd !== usersDB[username]["password"]
            return false
        else
            return true
        end
    end

    export transaction_auth, verify_userPWD, verify_userID

end