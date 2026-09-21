# Shared includes and presets for the scripts/ and scripts/FigureScripts/ entry points.

# --- Project Modules ---
include("../src/Data_import.jl")
include("../src/Scenario_creation.jl")
include("../src/Imbalance_functions.jl")
include("../src/Game_theoretic_functions.jl")
include("../src/Plotting_functions.jl")
include("../src/Types.jl")
include("../src/Export_functions.jl")

# Named presets for which allocation mechanisms to calculate.
const ALLOCATION_PRESETS = Dict(
    :default => ["shapley", "MCC", "VCG", "gately", "marginal_price", "flat_rate"],
    :all => ["shapley", "MCC", "MCC_budget_balanced", "VCG", "gately", "gately_interval", "marginal_price", "reduced_cost", "nucleolus", "flat_rate", "scaled"],
)

# Named presets for which clients to exclude from the analysis. These are applied on top of
# whatever load_data() returns, which is already restricted to clients with complete data,
# so the resulting portfolio size depends on the data snapshot in data/private/.
const CLIENT_EXCLUSION_PRESETS = Dict(
    :none => String[],                               # keep every client with complete data
    :drop_smallest_2 => ["X", "W"],                  # drop the 2 smallest by total demand
    :drop_smallest_3 => ["X", "W", "N"],             # drop the 3 smallest by total demand
    :nucleolus_subset => ["F", "V", "J", "E", "T", "O", "Y"], # small enough for nucleolus to remain tractable
)
