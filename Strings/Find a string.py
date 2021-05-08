def count_substring(s, sub):
    return sum(s[start:start+len(sub)] == sub for start in range(len(s)));

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)