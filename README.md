<div>
  <img src="https://github.com/elghallali/my-images/blob/master/Faculty%20Official/fsjest.jpg" title="fsjest" alt="fsjest" width="150" height="150" align="left"/>
  <img src="https://github.com/elghallali/my-images/blob/master/Faculty%20Official/uae.png" title="UAE" **alt="UAE" width="150" height="150" align="right"/>
</div>
<br><br>
<br><br>
<br><br>
<div align="center">
  <img src="https://github.com/elghallali/my-images/blob/master/Faculty%20Official/logo.png" title="DSDS" alt="DSDS" width="400" height="150"/>
</div>

<br>
<br>
<div align="center">

# IRY Tech

</div>

<br><br><br>
<div>
  <div align="left">

### Carried out by

| Student Name   |      APOGEE      |  CNE |
|----------|:-------------:|:------:|
| Issam EL MEHDI |  22017585 | P110127478 |
| Rabia AISSAOUI SLAOUI |    19005290   |   P149016790 |
| Yassine EL GHALLALI | 22017586 |    Z196800709 |

  </div>

  <div align="right">

### Framed by : Lotfi EL AACHAK

  </div>
</div>

### Note

> **Dear Reader**,
>
> I hope this note finds you well. I wanted to remind you that all the documents and application web that you have been using are meant for study purposes only. It's important to keep in mind that these resources should not be used for any illegal or unethical activities.
>
> Furthermore, it's crucial to respect the copyrights and intellectual property rights of the owners of these resources. As such, please refrain from distributing, sharing or using these materials for any commercial or personal gain.
>
> I encourage you to use these resources responsibly and make the most out of them for your academic and personal growth. Keep in mind that knowledge is power, and the more you learn, the better equipped you will be to face any challenges that come your way.
>
>Best regards,
>
> <div align="right"><strong>Our Team</strong></div>

## :bookmark_tabs: Description

> In today's digital age, e-commerce has become an integral part of our daily lives. With the growing popularity of online shopping, it's no surprise that many businesses have turned to e-commerce as a way to reach a wider audience and expand their customer base. One such business is **IRY Tech**, an e-commerce project that specializes in the sale of electronic materials such as appliances, televisions, cameras, and computers.
>
> **IRY Tech** is an innovative e-commerce platform that offers a wide range of electronic materials at competitive prices. The platform is designed to provide customers with a seamless and convenient shopping experience. Whether you are looking to purchase a new laptop, a high-definition television, or a top-of-the-line camera, **IRY Tech** has got you covered.
>
> One of the key features that sets **IRY Tech** apart from other e-commerce platforms is its user-friendly interface. The platform is easy to navigate, and customers can quickly find what they are looking for without having to sift through countless pages. The search function is intuitive and can help customers narrow down their search to find the exact product they need.
>
> Another feature that makes **IRY Tech** a top choice for online shoppers is its robust customer support. The team at **IRY Tech** is dedicated to providing excellent customer service, and they are always available to answer any questions or concerns that customers may have. Whether you need assistance with placing an order or have a question about a product, the customer support team is always happy to help.
>
> In addition to its user-friendly interface and excellent customer support, **IRY Tech** also offers a wide range of payment options. Customers can choose to pay with a credit card, debit card, or through a third-party payment platform such as **PayPal**. This flexibility ensures that customers can complete their transactions with ease and convenience.
>
> Finally, **IRY Tech** is committed to providing its customers with high-quality products at competitive prices. The platform works with some of the most reputable manufacturers in the industry to ensure that customers receive products that are reliable, efficient, and durable. **IRY Tech** also regularly updates its inventory to keep up with the latest trends and technologies in the industry, so customers can always find the newest and most innovative products.
>
> In conclusion, **IRY Tech** is an exceptional e-commerce platform that offers a wide range of electronic materials at competitive prices. Its user-friendly interface, robust customer support, and flexible payment options make it a top choice for online shoppers. If you're in the market for electronic materials, be sure to check out **IRY Tech** for all your shopping needs.

## :chains: Development

---

### :hammer_and_wrench: Development Tools

<br>
<div align="center">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-original-wordmark.svg" title="MySQL" **alt="MySQL" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original-wordmark.svg" title="VSCode" alt="VSCode" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg"  title="CSS3" alt="CSS" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original-wordmark.svg" title="HTML5" alt="HTML" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" title="JavaScript" alt="JavaScript" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-original-wordmark.svg" title="Bootstrap" alt="Bootstrap" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original-wordmark.svg" title="Git" **alt="Git" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/github/github-original-wordmark.svg" title="GitHub" **alt="GitHub" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-plain-wordmark.svg" title="Docker" alt="Docker" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/figma/figma-original.svg" title="Figma" alt="Figma" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/markdown/markdown-original.svg" title="Markdown" alt="Markdown" width="50" height="50"/>&nbsp;
</div>
<br>

---

### :wrench: Class Diagram

```mermaid
classDiagram
    class Product{
        id: int
        title: string
        selling_price : float
        discounted_price : float
        description : string
        category: string
        image_url : string
    }
    class Cart{
        id: int
        quantity: int
        user : User
        product : Product
    }
    class User{
        id: int
        email: string
        username : string
        last_name : string
        last_name : string
        password : string
        is_activate : boolean
        is_staff : boolean
        is_superuser : boolean
        date_joined : Date
        last_login : Date
    }
    class Customer{
        id: int
        name: string
        locality : string
        city : string
        mobile : int
        state : string
        zipcode : int
        user : User
    }
    class PostMessageContact{
        id: int
        name: string
        email : string
        content : string
        created : Date
    }
    class UserGroups{
        id: int
        user: User
        group : Group
    }
    class Group{
        id: int
        name: string
    }
    Cart "1" .. "1..*" Product
    Cart "1..*" .. "1" User
    Customer "*" .. "1" User
    UserGroups "1..*" .. "*" User
    UserGroups "1..*" .. "*" Group
```

---

### :clipboard: Design

---

### :gear: deployment

#### Crreate a new folder named `eShop` and open it with `Command Prompt`, `Terminal` or `VSCode`

> If you opened it with `VSCode` then open its terminal and do the following instructions to complete!

#### Download this application using `git`

```cmd
git clone https://github.com/elghallali/eShop.git .
```

#### Create a virtuial environment

```cmd
python -m venv env
```

#### Activate the virtuial environment

```cmd
.\env\Scripts\activate
```

#### Install requirements

```cmd
pip install -r requirements.txt 
```

#### Editing the settings.py file

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'data',
        'USER': 'root',
        'PASSWORD': '', # PASSWORD is the root password (is empty if your root doesn't have a password)
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
#### :warning: Create a database named `data` using `MySQL Workbench`, `MySQL Command Line` or `phpMyAdmin` :warning:

#### Create migrations

```cmd
python manage.py makemigrations
```

#### Migrate migrations

```cmd
python manage.py migrate
```

#### Create superuser

```cmd
python manage.py createsuperuser
```

#### Run the server

```cmd
python manage.py runserver
```

---

### :computer: Application

---

## :office: Conclusion
