import subprocess, re
def subproces_cmd_prep(cmd):
    # check= subprocess.check_output([cmd, "-p"])
    with open('tmp.dat', 'w') as f:
        check=subprocess.call(cmd,stdout= f,shell=True)
    with open('tmp.dat', 'r') as f:
        l = f.readlines()[4:]
        r = ''
        for i in l:
            c= re.findall(r'\|\-.*\:', i)
            if c:
                r = r + c[0].replace(r'|-', '').replace(':', ',')
        print(r)
    return check

if __name__ == '__main__':
    # subproces_cmd_prep('gcloud config list')
    t = input("Enter the table name ")
    print (subproces_cmd_prep('bq show {}'.format(t)) )
