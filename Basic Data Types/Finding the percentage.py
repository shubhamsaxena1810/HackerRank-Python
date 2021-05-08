if __name__ == '__main__':
    n = int(input())
    student_marks = list()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        lst=list()
        lst.append(name)
	lst.append(sum(scores))
        student_marks.append(lst)
         
    query_name = input()
    for i in range(0,len(student_marks)):
        if student_marks[i][0]==query_name:
            print("{0:.2f}".format(student_marks[i][1]/3))
