include("./database.jl")
include("./models.jl")

using .database: add_user, read_user
using .models: User


mike = User("Michael", "mike@python.com", "micheofire", "07000000009", "mike.fire")

add_user(mike)

# using DataFrames

# result = read_user(Dict("name" => "Michael"))

# for row in result
#     println(row)
# end

using SQLite

db = SQLite.DB("MILESTONE_DB")

query = "SELECT * from `Milestone_Users`"

DBInterface.execute(db, query)