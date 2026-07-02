

# problem 1

def calculate_bill(kwh: int) -> float:

    # calculate higher tiers first, adding in max from lower tiers

    bill = 0.0

    if kwh <= 0:
        return bill
    
    # tier1 full => 500 * .1 = 50
    # tier2 full => 500 * .15 = 75

    if kwh > 1000:
        bill += (kwh - 1000) * .2
        bill += 50 + 75
    elif kwh > 500: # also <= 1000
        bill += (kwh - 500) * .15
        bill += 50
    elif kwh <= 500: 
        bill += kwh * .1

    return bill



# problem 2

transactions = [
    "alice",
    "bob",
    "alice",
    "charlie",
    "bob",
    "alice"
]


def most_transactions(transactions: list[str]) -> list[str]:

    # scan thru list, creating count-hash, order by counts & return highest

    counts = {}

    for trans in transactions:
        counts[trans] = counts.get(trans, 0) + 1

    transList = list(counts.items())

    transList.sort(key=lambda item: item[1], reverse=True)

    highest_trans_count = transList[0][1]

    result = []

    # also return ties for highest count
    for trans in transList:
        if trans[1] == highest_trans_count:
            result.append(trans[0])
        else:
            break

    return result

print(most_transactions(transactions))




# problem 3


# merge ids with same email into dict {email, id}

itemz = [
    {"id": 1, "email": "a@test.com"},
    {"id": 2, "email": "b@test.com"},
    {"id": 3, "email": "a@test.com"}
]


def merge_duplicates(items: list[dict]) -> dict[str, any]:

    # scan thru list, adding to dict, return dict

    result = {}

    for item in items:
        email = item["email"]
        id = item["id"]
        
        result[email] = result.get(email, []) + [id]

    return result

print(merge_duplicates(itemz))




# problem 4

requests = [1, 2, 3, 10, 11, 20]


def rate_limit(timestamps: list[int]) -> list[int]:

    # scan thru list, checking 3-slot window for hi - lo <= 5
    # return all hi's where hi - low <= 5

    result = []

    if len(timestamps) < 4:
        return result

    hi = timestamps[2]
    lo = timestamps[0]
    if hi - lo <= 5:
        result.append(hi)

    for i in range(3, len(timestamps)):
        hi = timestamps[i]
        lo = timestamps[i - 3]
        if hi - lo <= 5:
            result.append(hi)

    return result




# problem 5

tickets = [
    {"id": 1, "priority": "high", "age": 2},
    {"id": 2, "priority": "low", "age": 10},
    {"id": 3, "priority": "high", "age": 1}
]

def sort_tickets(tickets: list[dict[str, any]]) -> list[dict[str,any]]:

    # break list into 3 chunks, sort each chunk, re-combine lists

    prio_h = [x for x in tickets if x["priority"] == "high"]
    prio_l = [x for x in tickets if x["priority"] == "low"]

    prio_h.sort(key=lambda item: item["age"], reverse=True)
    prio_l.sort(key=lambda item: item["age"], reverse=True)

    result = prio_h + prio_l

    return result








def valid_parenths(s: str):
    # create stack, add/pop as you see parenths in the string & check for correctness

    if not s:
        return True
    
    stack = []

    valid = {'[' : ']', '{' : '}', '(' : ')'}

    for ch in s:
        if ch in valid:
            stack.append(valid[ch])
        else:
            if not stack or ch != stack.pop():
                return False
            

    if not stack:
        return True
    else:
        return False

# parenthesis check problem
def check_parenths(s: str) -> bool:

    stack = []

    matches = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    for c in s:
        
        if c in matches:
            stack.append(matches[c])
        else:
            if not stack or stack.pop() != c:
                return False
        
    if not stack:
        return True
    else:
        return False
        
        








# 1 given a list of reading, find the avg

readings = [100, 120, 90, 110]


def find_avg(nums: list[int]) -> float:
    if not nums or len(nums) < 1:
        return 0.0
    
    total = 0
    for num in nums:
        total += num
    
    return total / len(nums)







# 2 find duplicate meter ids

meter_ids = [
    "M001",
    "M002",
    "M001",
    "M003",
    "M002"
]



def find_dups(meter_ids: list[str]) -> list[str]:
    # create counts-hash, build result from all counts > 1
    if not meter_ids:
        return []
    
    counts = {}

    for item in meter_ids:
        counts[item] = counts.get(item, 0) + 1

    result = [meter_id for meter_id, count in counts.items() if count > 1]

    return result

def find_dups(ids: list[str]) -> list[str]:
    dups = []
    
    if not ids or len(ids) < 1:
        return dups
    
    counts = {}
    for id in ids:
        counts[id] = counts.get(id, 0) + 1

    return [id for id, count in counts.items() if count > 1]















# 3 group readings by customer

readings = [
    ("cust1", 100),
    ("cust2", 150),
    ("cust1", 125),
    ("cust2", 175),
    ("cust3", 200)
]

{
    "cust1": [100, 125],
    "cust2": [150, 175],
    "cust3": [200]
}

def grp_readings(reads: list[tuple[str, int]]) -> dict[str, list[int]]:
    result = {}
    if not reads:
        return result
    
    for read in reads:
        if read[0] not in result:
            result[read[0]] = []

        result[read[0]].append(read[1])

    return result









# find the top 3 customers by usage

usage = {
    "cust1": 1500,
    "cust2": 2100,
    "cust3": 1800,
    "cust4": 900,
    "cust5": 3000
}

def top_usage(uses: dict[str, int]) -> list[tuple[str, int]]:
    if not uses:
        return []
    
    sorted_uses = list(uses.items())

    sorted_uses.sort(key=lambda x: x[1], reverse = True)

    return sorted[:3]




# find valid readings (between 0 and 1000)

readings = [100, -5, 150, 9999, 200, -10]

def valid_readings(reads: list[int]) -> list[int]:

    if not reads:
        return []
    
    valid = list(filter(lambda x: x > 0 and x < 1000, reads))

    return valid



# convert usage strings to ints
usage = ["100", "250", "75", "300"]

def convert_str_to_int(uses: list[str]) -> list[int]:

    if not uses:
        return []
    
    ints = list(map(lambda x: int(x), uses))

    return ints



def sum_two_indicies(nums: list[int], target: int) -> tuple[int, int] | None:
    # keep track of what's seen and what's needed, scan thru once

    if not nums or len(nums) < 2:
        return None
    
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return (i, seen[needed])
        
        seen[num] = i

    return None

# 1 two sum indicies (unsorted)

def two_sum_indices(nums: list[int], target: int) -> tuple[int, int] | None:
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return (seen[needed], i)

        seen[num] = i

    return None
        


def merge_intervals(intervals: list[list[int]]) -> list[list[int]] | None:
    # sort intervals, scan thru looking for overlapping & build new result
    
    if not intervals:
        return None

    result = []

    intervals = sorted(intervals, key=lambda x: x[0])

    last_int = intervals[0]

    for interval in intervals[1:]:
        if interval[0] < last_int[1]:
            last_int = [last_int[0], max(last_int[1], interval[1])]
        else:
            result.append(last_int)
            last_int = interval

    result.append(last_int)

    return result
        

# 2 merge time intervals


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    # scan through pairs looking for position 0 inside the current interval, create merged result along the way

    if not intervals:
        return []
    
    intervals = sorted(intervals, key=lambda x: x[0])

    result = []
    prev_int = intervals[0]

    for interval in intervals[1:]:
        if interval[0] < prev_int[1]:
            prev_int = [
                prev_int[0],
                max(prev_int[1], interval[1])
            ]
        else:
            result.append(prev_int)
            prev_int = interval
        
    result.append(prev_int)

    return result



def first_non_rep(s: str) -> int:
    # create counts hash, scan through looking for char with count == 1

    if not s:
        return -1
    
    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
        
    return -1


# 3 first non-repeating character

def first_non_rep_char(s: str) -> int:
    # create a counts hash for each char then return the first char with a non-1 value

    if not s:
        return -1
    
    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
        
    return None


