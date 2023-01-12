# plotly holiday app building challenge

This app was developed for plotly holiday application building competition. 
1. view app deployed on aws elastic beanstalk 
    ### http://plotly-holiday-app-build-dev.us-west-2.elasticbeanstalk.com/

2. view deployment of application on render.com 
    ### https://customer-churn-dashboard.onrender.com/

application screenshots and implementation
![Screenshot from 2023-01-13 00-11-56](https://user-images.githubusercontent.com/42097653/212153928-a3a96d48-3cd8-4684-a240-5ae605071155.png)
![Screenshot from 2023-01-13 00-12-44](https://user-images.githubusercontent.com/42097653/212153948-0af4d4cb-8df9-443d-8b12-3686279fbc81.png)
![Screenshot from 2023-01-13 00-13-00](https://user-images.githubusercontent.com/42097653/212153956-2534ea38-f8ec-4abf-9a2c-c4ae61513d77.png)
![Screenshot from 2023-01-13 00-13-17](https://user-images.githubusercontent.com/42097653/212153965-f4cac816-16a2-4574-b72f-056adb8d393a.png)
![Screenshot from 2023-01-13 00-13-22](https://user-images.githubusercontent.com/42097653/212153975-f066f7ad-0f5b-44d3-871f-02db545c6323.png)
![Screenshot from 2023-01-13 00-13-24](https://user-images.githubusercontent.com/42097653/212153977-636d62a6-7131-4b07-afad-368dacc0b19b.png)
![Screenshot from 2023-01-13 00-13-33](https://user-images.githubusercontent.com/42097653/212153994-09a4bf64-3072-402a-92f5-ce38c6830955.png)
![Screenshot from 2023-01-13 00-13-49](https://user-images.githubusercontent.com/42097653/212154004-dbcb60e3-b174-44f6-89b5-9553083ab6ad.png)


for reproducing the app on local: 
Python version: 3.7.15
for running and installation
1. Clone the repository

```
    git clone https://github.com/someshfengde/plotly_holiday_app_build.git
```

2. install requirements **make sure you have python 3.7.15 (for other versions make sure you update pycaret and dash version) 

```
    pip install -r requirements.txt
```
3. start the application

`deployment server`
```
    gunicorn application:application
```

`development server`
```
    python3 application.py
```

I've deployed the applcation on AWS Elastic beanstalk 
Thank you [@WenjieZ](https://github.com/WenjieZ) for making this guide, It really helped me for deploying this application:

link to the guide: https://www.zhengwenjie.net/beanstalk/

### TODO:
- [ ] add video implementation
