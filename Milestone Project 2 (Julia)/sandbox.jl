# include("./database.jl")
# include("./models.jl")

# using .database: add_user, read_user
# using .models: User


# mike = User("Michael", "mike@python.com", "micheofire", "07000000009", "mike.fire")

# add_user(mike)

# using DataFrames

# result = read_user("username", Dict("name" => "Michael"))

# for row in result
#     println(row)
# end

# using SQLite

# db = SQLite.DB("MILESTONE_DB")

# query = "SELECT * from `Milestone_Users`"

# DBInterface.execute(db, query)

 #+ "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}")


function validate_domain_name(domain_name)

    regex = "^((?!-)[A-Za-z0-9-]" * "{1,63}(?<!-)\\.)" * "+[A-Za-z]{2,6}"
    regex = Regex(regex)
    
    if domain_name === nothing
        return false
    end
    
    if occursin(regex, domain_name)
        return true
    else
        return false
    end
end

validate_domain_name("nhub.co")