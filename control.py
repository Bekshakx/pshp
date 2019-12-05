## THIS IS THE CCONTROLLER FILE< IT IS TH SUPERSET SUPER FATHER OF THE MODULE AND VIEW IT THIS PROJECT
import time
import settings
import platform
import subprocess
import view
import module
import sys
from pyzt import inputs, inputi, inputf

def logger(message):
    time_format  = "%Y-%m-%d %X %A %B %p %r"
    time_current = time.strftime(time_format)
    with open('data/log.txt','a') as f:
        f.write(f"{message}")
        f.write('\n')


class Control():
    f_list=[]
    fr = settings.FIRST_RUN
    current_user = 'Azat' #Current user in this session
    current_user_role = 'admin'

    def prepare_file(self,log='data/log.txt',users='data/users.txt',products='data/products.txt',orders='data/orders.txt'):
        path_list = [log,orders,products,users]
        for each in path_list:
            with open(each,'w') as f:
                f.write('')

    def system_check(self):
        # check python version
        print(f"Step 1: Checking Python Version : {platform.python_version()}")
        if platform.python_version()[0] == '3':
            print('PYTHON VERSION OK!')
        else:
            exit('Sorry, The program dose not support your python version, please update to python3.x')
        # check required packages installed
        print(f"Step 2: Checking Python packages")
        required_pkgs = ['azt','pyzt']
#         installed_pkgs = subprocess.check_output(['pip3','list']).decode("utf-8")
        for pkg in required_pkgs:
#             if pkg not in installed_pkgs:
#                 exit("requirements not installed! Please install all of required packages.")
            print("PYTHON PACKAGE REQUIREMENTS OK!")
        print(f"Step 3: Checking data resources")
        data_resources = ['data/log.txt','data/users.txt','data/products.txt','data/orders.txt']
        for each in data_resources:
            try:
                with open(each) as f:
                    pass
            except FileNotFoundError:
                exit("Data Source NOt Found!")
    def login(self):
        f_list=[]
        while True:
            username=inputs('username: ')
            pwd=inputs('password: ')
            with open('data/users.txt','r') as f:
                d=f.read().split('\n')
                d.pop()
            for i in d:
                f1=i.split(',')
                f_list.append(f1)
            for item in range(len(f_list)):
                    if f_list[item][0] ==username and f_list[item][1] ==pwd and f_list[item][3]=='True':
                        time_format  = "%Y-%m-%d %X %A %B %p %r"
                        time_current = time.strftime(time_format)
                        with open('data/log.txt','a') as f:
                            f.write(f"{'Кірген уақыты : '}{f_list[item][0]}: {'Admin'}: {time_current}")
                            f.write('\n')
                        self.admin()
                    elif f_list[item][0] ==username and f_list[item][1] ==pwd and f_list[item][5]=='True':
                        time_format  = "%Y-%m-%d %X %A %B %p %r"
                        time_current = time.strftime(time_format)
                        with open('data/log.txt','a') as f:
                            f.write(f"{'Кірген уақыты : '}{f_list[item][0]}: {'Client'}: {time_current}")
                            f.write('\n')
                        self.Client()
                    elif f_list[item][0] ==username and f_list[item][1] ==pwd and f_list[item][4]=='True':
                        time_format  = "%Y-%m-%d %X %A %B %p %r"
                        time_current = time.strftime(time_format)
                        with open('data/log.txt','a') as f:
                            f.write(f"{'Кірген уақыты : '}{f_list[item][0]}: {'Staff'}: {time_current}")
                            f.write('\n')
                        self.staff()
                    elif f_list[item][0] ==username and f_list[item][1] ==pwd and f_list[item][6]=='True':
                        time_format  = "%Y-%m-%d %X %A %B %p %r"
                        time_current = time.strftime(time_format)
                        with open('data/log.txt','a') as f:
                            f.write(f"{'Кірген уақыты : '}{f_list[item][0]}: {'Manager'}: {time_current}")
                            f.write('\n')
                        self.manager()


    def logout(self):
        while True:
            settings.CURRENT_USER_ROLE=""
            home_admin = view.Home()
            home_admin.welcome()
            k=inputs("Registration '1' and Login '2'")
            if k=='1' and settings.FIRST_RUN==True:
                self.Regis()
                self.Client()
            elif k=='2':
                self.login()
            else:
                print('kayta engiz')


    def run(self):
        print("Running the AzatAI Python Shop system self checking")
        self.system_check()
        self.prepare_file()
        if self.fr is False: # super admin already exist
            print("In the case super admin already exist")
            # TODO
        else:
            home = view.Home()
            home.superadmin()
            user_name = inputs('Please input a username for SUPERADMIN:\n')
            user_pw = inputs(f'Please input a password for SUPERADMIN {user_name}:\n')
            user = module.User()
            user.is_admin = True
            user.add(user_name,user_pw)
            settings.SUPER_ADMIN = user_name
            settings.SUPER_ADMIN_PW = user_pw
            settings.CURRENT_USER = user_name
            settings.CURRENT_USER_ROLE = "ADMIN"
            self.admin()


    def Regis(self):
        aty=inputs(" login : ")
        parol=inputs("parol: ")
        user = module.User()
        user.is_client=True
        user.add(aty,parol)
        settings.CURRENT_USER_ROLE='Client'
    
    def Client(self):
        while True:
                    user = module.User()
                    user.is_client=True
                    settings.CURRENT_USER_ROLE="Client"
                    home_admin = view.Home()
                    home_admin.welcome()
                    tauar_tizim=[]
                    new_tauar=[]
                    with open('data/tauarlar_tizimi.txt','r+') as e:
                        r=e.read()
                        r_split=r.split('\n')
                        r_split.pop()
                    for each in r_split:
                        r2_split=each.split("-")
                        new_tauar.append(tuple(r2_split))
                    for index,item in enumerate(new_tauar):
                        print(index,item)
                    while True:
                        sh=inputs(' жалғастырғыңыз келсе "1" ,  logout "2", basty bet "3" : ')
                        if sh=='1':
                            sum_list=[]
                            sum=0
                            st=True
                            karzhy=inputi(" Қаржы көлемін енгізіңіз : ")
                            while True:
                                for index,item in enumerate(new_tauar):
                                    print(index,item)
                                client_zh=inputs(' жалғастырғыңыз келсе "1" , тоқтатқыңыз келсе "2": ')
                                if client_zh=='1':
                                    client_t=inputi("Сатып алғыңыз келетін тауар номерін енгізіңіз : ")
                                    if client_t<len(new_tauar) and client_t>=0:
                                        t_tizim=new_tauar[client_t]
                                        if int(t_tizim[1])<=karzhy:
                                            sum+=int(t_tizim[1])
                                            sum_list.append(sum)
                                            if st:
                                                while st:
                                                    tauar_tizim.append(t_tizim)
                                                    karzhy-=int(t_tizim[1])
                                                    u=subprocess.check_output('date').decode('utf-8')
                                                    tauar_tizim.append(u)
                                                    print(f" Алған тауарыңыз {t_tizim}, сізде қалған қаржыңыз {karzhy}")
                                                    st=False
                                            elif sum>200000:
                                                tauar_tizim.append(t_tizim)
                                                print('Сіз біздің VIP клиентіміз болдыңыз, сізде 15% жеңілдік бар')
                                                karzhy-=(int(t_tizim[1])-int(t_tizim[1])*0.15)
                                                u=subprocess.check_output('date').decode('utf-8')
                                                tauar_tizim.append(u)
                                                print(f" Алған тауарыңыз {t_tizim}, сізде қалған қаржыңыз {karzhy}")
                                        else:
                                             print(f'Кешіріңіз сіздің қаржыңыз тауарды алуға жеткіліксіз !!!')
                                    else:
                                        print('Қате шықты қайта енгізіңіз : ')
                                elif client_zh=='2':
                                    if sum==0:
                                        break
                                    elif sum>0:
                                        name='Сатып алынған тауар тізімі'
                                        print(f''' \n\n1mall online дүкенінен сауда жасағаныңызға көп рахмет !!!
                             {name.center(50,'-')}
                             '''+'\n')
                                        for i in range(0,len(new_tauar),2):
                                            print(new_tauar[i])
                                        j='❤❤❤'
                                        print(f''' {j.center(50,"-")} ''')
                                        print(f" Total : {sum} \n Time: {subprocess.check_output('date').decode('utf-8')} \n     Қолдау көрсеткен компания \n {subprocess.check_output('azt').decode('utf-8')}")
                                        with open('tauarr','a') as f:
                                                for i in new_tauar:
                                                    f.write(str(i)+'\n')
                                        sh=inputs(' жалғастырғыңыз келсе "1" ,  logout "2" , basty bet "3" :  ')
                                        if sh=='1':
                                            pass
                                        elif sh=='2':
                                            self.end()
                                            view.Home()
                                            self.logout()
                                        elif sh=='3':
                                            self.Client()
                        elif sh=='2':
                            self.end()
                            view.Home()
                            self.logout()
                        elif sh=='3':
                            self.Client()
    
    def end(self):
            time_format  = "%Y-%m-%d %X %A %B %p %r"
            time_current = time.strftime(time_format)
            with open('data/log.txt','a') as f:
                f.write(f"{'Шыққан уақыты:'} {settings.CURRENT_USER_ROLE}: {time_current}")
                f.write('\n')

    def staff(self):
        while True:
            user = module.User()
            user.is_staff=True
            settings.CURRENT_USER_ROLE="Staff"
            home_admin = view.Home()
            home_admin.welcome()
            sh=inputs(' жалғастырғыңыз келсе "1" ,  logout "2" , basty bet "3" : ')
            if sh=='1':
                while True:
                        q=inputs(' тауарларды көргіңіз келсе "1" , тауар қосқыңыз келсе "2", тауар бағасын өзгерткіңіз келсе "3" , logout "4" , basty bet "5" : ')
                        if q=='1':
                            new_tauar=[]
                            with open('data/tauarlar_tizimi.txt','r+') as e:
                                r=e.read()
                                r_split=r.split('\n')
                                r_split.pop()
                            for each in r_split:
                                r2_split=each.split("-")
                                new_tauar.append(tuple(r2_split))
                            for index,item in enumerate(new_tauar):
                                print(index,item)
                        elif q=='2':
                            new_tauar=[]
                            with open('data/tauarlar_tizimi.txt','r+') as e:
                                r=e.read()
                                r_split=r.split('\n')
                                r_split.pop()
                            for each in r_split:
                                r2_split=each.split("-")
                                new_tauar.append(tuple(r2_split))
                            for index,item in enumerate(new_tauar):
                                print(index,item)
                            while True:
                                t_engizu=inputs(' тауар енгізгіңіз келсе "1" , тоқтатқыңыз келсе "2": ')
                                if t_engizu=='1':
                                    t_list=[]
                                    tauar_aty=inputs(" тауар атын енгізіңіз : ")
                                    tauar_bagasy=inputf(" тауар бағасын енгізіңіз : ")
                                    t_list.append(tauar_aty)
                                    t_list.append(tauar_bagasy)
                                    new_tauar.append(tuple(t_list))
                                    for index,i in enumerate(new_tauar):
                                        print(index,i)
                                    with open('data/tauarlar_tizimi.txt','w') as f:
                                        for i in new_tauar:
                                            f.write(str(i[0])+ '-' +str(i[1]) +'\n')
                                elif t_engizu=='2':
                                    break
                        elif q=='3':
                            new_tauar=[]
                            with open('data/tauarlar_tizimi.txt','r+') as e:
                                r=e.read()
                                r_split=r.split('\n')
                                r_split.pop()
                            for each in r_split:
                                r2_split=each.split("-")
                                new_tauar.append(tuple(r2_split))
                            for index,item in enumerate(new_tauar):
                                print(index,item)

                            x=inputi(" Өзгертетін тауар нөмірін енгізіңіз : ")
                            for index,i in enumerate(new_tauar):
                                if x==index:
                                    tauar_bagasi=inputs(" тауар бағасын енгізіңіз : ")
                                    e=list(new_tauar[x])
                                    e[1]=tauar_bagasi
                                    e1=tuple(e)
                                    new_tauar.insert(x,e1)
                                    del new_tauar[x+1]
                                    for index, i in enumerate(new_tauar):
                                        print(index,i)
                                    with open('data/tauarlar_tizimi.txt','w') as f:
                                        for i in new_tauar:
                                            f.write(str(i[0])+ '-' +str(i[1]) +'\n')
                        elif q=='4':
                            self.end()
                            view.Home()
                            self.logout()
                        elif q=='5':
                            self.staff()
            elif sh=='2':
                    self.end()
                    view.Home()
                    self.logout()
            elif sh=='3':
                self.staff()
    def manager(self):
         while True:
            user = module.User()
            user.is_manager=True
            settings.CURRENT_USER_ROLE="Manager"
            home_admin = view.Home()
            home_admin.welcome()
            sh=inputs(' жалғастырғыңыз келсе "1" ,  logout "2" , basty bet "3" : ')
            if sh=='1':
               while True:
                q=inputs('''тауарларды көргіңіз келсе "1" , сатылған тауарды көргіңіз келсе "2", тауардың бірін өшіргіңіз келсе "3", logout "4" , basty bet "5" : ''')
                if q=='1':
                    new_tauar=[]
                    with open('data/tauarlar_tizimi.txt','r+') as e:
                        r=e.read()
                        r_split=r.split('\n')
                        r_split.pop()
                    for each in r_split:
                        r2_split=each.split("-")
                        new_tauar.append(tuple(r2_split))
                    for index,item in enumerate(new_tauar):
                        print(index,item)
                elif q=='2':
                    with open('tauarr','r') as f:
                            g=f.read()
                            print(g)
                elif q=='3':
                    new_tauar=[]
                    new1_tauar=[]
                    with open('data/tauarlar_tizimi.txt','r+') as e:
                        r=e.read()
                        r_split=r.split('\n')
                        r_split.pop()
                    for each in r_split:
                        r2_split=each.split("-")
                        new_tauar.append(tuple(r2_split))
                    for index,item in enumerate(new_tauar):
                        print(index,item)
                    x=inputi(" Жоятын тауар номерін енгізіңіз : ")
                    for index,item in enumerate(new_tauar):
                        if x==index:
                            new_tauar.remove(new_tauar[index])
                            for each in new_tauar:
                                new1_tauar.append(each)
                            for index,i1 in enumerate(new1_tauar):
                                print(index,i1)
                            with open('data/tauarlar_tizimi.txt','w') as f:
                                for i in new1_tauar:
                                    f.write(str(i[0])+ '-' +str(i[1]) +'\n')
                elif q=='4':
                    self.end()
                    view.Home()
                    self.logout()
                elif q=='5':
                    self.manager()
            elif sh=='2':
                self.end()
                view.Home()
                self.logout()
            elif sh=='3':
                self.manager()

    def admin(self):
        while True:
            f_list=[]
            user = module.User()
            user.is_admin=True
            settings.CURRENT_USER_ROLE="ADMIN"
            home_admin = view.Home()
            home_admin.welcome()
            admin_choice = inputi("Please select your choice: logout - '1' , adamdar tizimin korginiz kelse - '2', adamdar kirgen jane wikkan uakiti-'3' : ")
            if admin_choice==1:
                view.Home()
                k=inputs("Registration '1' and Login '2'")
                if k=='1':
                    self.Regis()
                    self.Client()
                elif k=='2':
                    self.login()
            elif admin_choice==2:
                print("index, Login, Password, Create date,                                   admin, staff, client, manager")
                with open('data/users.txt','r') as f:
                    d=f.read().split('\n')
                    d.pop()
                for i in d:
                    f1=i.split(',')
                    f_list.append(f1)
                for index,each in enumerate(f_list):
                    print(index,each)
                # for index,item  in enumerate(range(len(f_list))):
                #     if f_list[item][5]=="True":
                #         print(index,f_list[item])
                oz=inputi(' Адам статусын өзгерткіңіз келсе "1", logout -- "2" ,basty bet -"3" : ')
                if oz==1:
                    try:
                        if len(f_list)>1:
                                x=inputi('Өзгертетін адамның index енгізіңіз: ')
                                while True:
                                        q=inputi('''Client-->Staff = '1',  Client-->manager = '2'
                                        Staff-->Manager = '3': ''')
                                        for index,i in enumerate(range(len(f_list))):
                                            if q==1 and f_list[i][5]=="True":
                                                    if x==index:
                                                        user = module.User()
                                                        f_list[i][4]='True'
                                                        user.is_staff=True
                                                        f_list[i][5]='False'
                                                        user.is_client=False
                                                        f_list.insert(x,f_list[x])
                                                        del f_list[x+1]
                                                        print("index, Login, Password, Create date,                                  admin, staff, client, manager")
                                                        for index, i1 in enumerate(range(len(f_list))):
                                                                print(index,f_list[i1])
                                                                with open('data/users.txt','w') as f:
                                                                    for i2 in range(len(f_list)):
                                                                        f.write(str(f_list[i2][0])+','+ str(f_list[i2][1])+','+ str(f_list[i2][2])+','+str(f_list[i2][3])+','+str(f_list[i2][4])+','+str(f_list[i2][5])+','+str(f_list[i2][6])+'\n')
                                                    g=inputs('logout "1", basty bet "2" , zhalgastiru "3" : ')
                                                    home_admin.list_user(3)
                                                    if g=='1':
                                                        self.end()
                                                        view.Home()
                                                        self.logout()
                                                    elif g=='2':
                                                        self.admin()
                                                    elif g=='3':
                                                        pass

                                            elif q==2 and f_list[i][5]=="True":
                                                    if x==index:
                                                        user = module.User()
                                                        f_list[i][6]='True'
                                                        user.is_manager=True
                                                        f_list[i][5]='False'
                                                        user.is_client=False
                                                        f_list.insert(x,f_list[x])
                                                        del f_list[x+1]
                                                        print("index, Login, Password, Create date,                                  admin, staff, client, manager")
                                                        for index, i1 in enumerate(range(len(f_list))):
                                                                print(index,f_list[i1])
                                                                with open('data/users.txt','w') as f:
                                                                    for i2 in range(len(f_list)):
                                                                        f.write(str(f_list[i2][0])+','+ str(f_list[i2][1])+','+ str(f_list[i2][2])+','+str(f_list[i2][3])+','+str(f_list[i2][4])+','+str(f_list[i2][5])+','+str(f_list[i2][6])+'\n')
                                                    g=inputs('logout "1", basty bet "2", Zhalgastiru "3" : ')
                                                    home_admin.list_user(3)
                                                    if g=='1':
                                                        self.end()
                                                        view.Home()
                                                        self.logout()
                                                    elif g=='2':
                                                        self.admin()
                                                    elif g=='3':
                                                        pass

                                            elif q==3 and f_list[i][4]=="True":
                                                    if x==index:
                                                            user = module.User()
                                                            f_list[i][6]='True'
                                                            user.is_manager=True
                                                            f_list[i][4]='False'
                                                            user.is_staff=False
                                                            f_list.insert(x,f_list[x])
                                                            del f_list[x+1]
                                                            print("index, Login, Password, Create date,                                  admin, staff, client, manager")
                                                            for index, i1 in enumerate(range(len(f_list))):
                                                                    print(index,f_list[i1])
                                                                    with open('data/users.txt','w') as f:
                                                                        for i2 in range(len(f_list)):
                                                                            f.write(str(f_list[i2][0])+','+ str(f_list[i2][1])+','+ str(f_list[i2][2])+','+str(f_list[i2][3])+','+str(f_list[i2][4])+','+str(f_list[i2][5])+','+str(f_list[i2][6])+'\n')

                                                    g=inputs('logout "1", basty bet "2" , Zhalgastiru "2": ')
                                                    home_admin.list_user(3)
                                                    if g=='1':
                                                        self.end()
                                                        view.Home()
                                                        self.logout()
                                                    elif g=='2':
                                                        self.admin()
                                                    elif g=='3':
                                                        pass

                                            elif q not in [1,2,3] and f_list[i][4]!="True" and f_list[i][5]!="True" and f_list[i][6]!="True":
                                                while True:
                                                    print(" Ozgeris zhasalmaidy , tomendegi nuskalardy tandaniz ")
                                                    g=inputs(' logout - "1", basty bet- "2" , zhalgastirgin kelse - "3" ')
                                                    home_admin.list_user(3)
                                                    if g=='1':
                                                        self.end()
                                                        self.logout()
                                                    elif g=='2':
                                                        self.admin()
                                                    elif g=='3':
                                                        pass






                        else:
                                    print(' Сайтқа тіркелген адам табылмады ')
                                    g=inputs(' logout - "1", basty bet- "2" ')
                                    home_admin.list_user(3)
                                    if g=='1':
                                        self.end()
                                        self.logout()
                                    elif g=='2':
                                        self.admin()

                    except(ValueError):
                        pass
                elif oz==2:
                        self.end()
                        view.Home()
                        self.logout()
                elif oz==3:
                        self.admin()


            elif admin_choice==3:
                while True:
                    with open('data/log.txt','r') as f:
                        d=f.read().split('\n')
                        d.pop()
                    for i in d:
                        f1=i.split(',')
                        f_list.append(f1)
                    for index,each in enumerate(f_list):
                        print(index,each)
                    g=inputs(' logout - "1", basty bet- "2" ')
                    home_admin.list_user(3)
                    if g=='1':
                        self.end()
                        self.logout()
                    elif g=='2':
                        self.admin()
                                        
