import psutil

def ProcessDisaply():
    listprocess =[]

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs  = ['pid' ,'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms/(1024 *1024)

            listprocess.append(pinfo)


        except(psutil.NosSUchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    return listprocess


def main():
    print("Marvellous Infosystems : Python AUTOMATION & Machine Learning")

    print("Process Monitor")

    listprocess = ProcessDisaply()

    for elem in listprocess:
        print(elem)

if __name__ == "__main__":
    main()