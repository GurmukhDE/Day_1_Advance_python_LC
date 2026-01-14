#-1 Count length by category

words = ["data", "python", "spark", "dbt", "aws"]
lengths = {w: len(w) for w in words}
print(lengths)

#---------------------------------------

#-2-Grouping Logic (Pre-Aggregation)
# — Count length by category

words = ["data", "python", "spark", "dbt", "aws"]
lengths = {w: len(w) for w in words}
print(lengths)

#----------------------------------------------------
# Useful when summarizing features, text length, etc.

#-3-Date / Time Zone Transform (Simulated)

#Suppose you have date strings:

dates = ["2025-01-01", "2025-02-10"]

#----------------------------------------------------

#-4- Extract years

years = [int(d.split("-")[0]) for d in dates]
print(years)  # [2025, 2025]
#------------------------------------------------

# -5 Date parsing is everywhere in pipelines.

#Nested List + Filtering (Real-World)

#You have log lines with comma-separated items:

logs = ["ERR,1001,timeout", "OK,2001,success", "ERR,1002,fail"]

Q13 — Just error codes
errors = [line.split(",")[1] for line in logs if line.startswith("ERR")]
print(errors)  # ['1001', '1002']

#----------------------------------------------------------------------------

#This is real log parsing logic.
#-6-Complex Condition with Data Cleanup

raw_values = [" 10", "none", "20", "", "30", "0"]
clean_nums = [int(x.strip()) for x in raw_values if x.strip().isdigit() and int(x.strip()) > 0]
print(clean_nums)  # [10, 20, 30]

#------------------------------------------------------------------------------------
