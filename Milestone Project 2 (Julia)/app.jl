include("./views.jl")
include("./Auth.jl")

using .views
using .Auth

printstyled(" Serving Nigeria, One Transaction at a time.\n Press any key to continue....... \n ==> "; color = :green)
readline()

login()
