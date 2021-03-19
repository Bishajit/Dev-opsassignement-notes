#And:both
#OR:at least one
#NOT: converts to opposite condition

has_good_credit  = True
has_criminal_credit  = False

if has_good_credit  and not has_criminal_credit:
    print("Eligible for loan")