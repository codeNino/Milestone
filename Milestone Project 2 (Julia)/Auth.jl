module Auth
    include("./database.jl")
    using .database

    clear() = run(`cmd /c cls`)


    function transaction_auth(pwd, username)
        token = 3
        while pwd !== read_user("password", Dict("username"=> username))
            println("Password Incorrect...\n You have $token attempt(s) left \n")
            println("Press 1 to Try Again or 2 to Quit\n ===>  ")
            global action = readline()
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
                if pwd === read_user("password", Dict("username"=> username))
                    println("Transaction Authenticated")
                    break
                end
            end
        end
    end



    function verify_userID(username)

        if read_user("username", Dict("username"=> username)) === nothing
            return false
        else
            return true
        end
    end


    function verify_userPWD(pwd, username)

        if pwd !== read_user("password", Dict("username"=> username))
            return false
        else
            return true
        end
    end

    function validate_domain_name(domain_name)

        let regex = "^((?!-)[A-Za-z0-9-]" * "{1,63}(?<!-)\\.)" * "+[A-Za-z]{2,6}"
        compiled_regex = Regex(regex)
        
        if domain_name === nothing
            return false
        end
        
        if occursin(compiled_regex, domain_name)
            return true
        else
            return false
        end
    end

    export transaction_auth, verify_userPWD, verify_userID, validate_domain_name

end