# IRY Tech :

## :bookmark_tabs: Description :


## :chains: Development :

### :hammer_and_wrench: Development Tools :

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-original-wordmark.svg" title="MySQL" **alt="MySQL" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original-wordmark.svg" title="VSCode" alt="VSCode" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg"  title="CSS3" alt="CSS" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" title="JavaScript" alt="JavaScript" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-original-wordmark.svg" title="Bootstrap" alt="Bootstrap" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original-wordmark.svg" title="Git" **alt="Git" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/github/github-original-wordmark.svg" title="GitHub" **alt="GitHub" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-plain-wordmark.svg" title="Docker" alt="Docker" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/figma/figma-original.svg" title="Figma" alt="Figma" width="40" height="40"/>&nbsp;
</div>

### :wrench: Class Diagram :

```mermaid
classDiagram
    class Product{
        id: int
        title: string
        seling_price : float
        discounted_price : float
        discription : string
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

### :clipboard: Design :

### :gear: development :

### :computer: Application :

## :office: Conclusion :
