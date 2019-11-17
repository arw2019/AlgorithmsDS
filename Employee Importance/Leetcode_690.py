# top 1.2%
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, employee_id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        S, I = {}, {}
        for employee in employees:
            I[employee.id] = employee.importance
            S[employee.id] = employee.subordinates
        
        def dfs(employee_id: int) -> int:
            return I[employee_id] + sum([dfs(e) for e in S[employee_id]])
        
        return dfs(employee_id)
