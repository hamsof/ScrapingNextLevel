function load_books(index){
    const book = document.createElement("div")
    book.classList.add("book_container","col-sm-4")
    book_data = index
    rating = Math.floor(Math.random() * 200 + 1)
    price = Math.floor(Math.random() * 7000 + 3000)

    //stars
    star = Math.floor(Math.random() * 6)
    var star_str="";
    for(let i=0;i<star;i++)
    {
        star_str+=`<span class="fa fa-star"></span>`
    }
    for(let i=0;i<5-star;i++)
    {
        star_str+=`<span class="fa fa-star not_filled"></span>`
    }
    star_data_ater = Math.random().toFixed(2);
    rate = +star+ +star_data_ater

    //stock
    stock_arr = [`<p class="stock in_stock " data-stock="in stock"><i class="fa fa-check" aria-hidden="true"></i> In stock</p>`,`<p class="stock not_stock " data-stock="not in stock"><i class="fa fa-times" aria-hidden="true"></i> Not in stock</p>`]
    stock_rand = Math.floor(Math.random() * 2)
    stock_str = stock_arr[stock_rand]
    //console.log(stock_str);
    
    book.innerHTML =
    `
        <img src="${book_data["imageLink"]}" alt="">
        <p  class="book_name"><a href="${book_data["link"]}" target="_blank"> ${book_data["title"]}</br> By ${book_data["author"]}</p></a></p>
        <div class="align-left">
            <p class=" price green">Rs.${price}</p>
            ${stock_str}
            <div class="stars" data-rate-star=${rate}>${star_str}</div>
            <p class="review green" data-rating="${rating}">${rating} Reviews</p>
            <button>Add to cart</button>
        </div>
    `
    container = document.getElementById("container")
    container.appendChild(book)
}

//getting id of the element that fired that event
//behtreen logic 

previous_elem = document.getElementById("page_1_parent")
var next_id = 2

function load_books_by_page(e)
{
    console.log(e.target.id);

    Id_fired = e.target.id;


    e.target.classList.add("active")
    previous_elem.classList.remove("active")

    r = document.getElementById("next_page")
    r.classList.remove("disabled")
    r.classList.add("active")

    previous_elem = e.target;

    var index_1;
    var index_2;

    next_button = document.getElementById("page_next")
    if(Id_fired == "page_1")
    {
        index_1 = 0;
        index_2 = 15;
        next_id = 2
    }
    if(Id_fired == "page_2")
    {
        index_1 = 15;
        index_2 = 30;
        next_id = 3
    }
    if(Id_fired == "page_3")
    {
        index_1 = 30;
        index_2 = 45;
        next_id = 4
    }
    if(Id_fired == "page_4")
    {
        index_1 = 45;
        index_2 = 60;
        next_id = 5
    }
    if(Id_fired == "page_5")
    {
        index_1 = 60;
        index_2 = 75;
        next_id = 6
    }
    if(Id_fired == "page_6")
    {
        index_1 = 75;
        index_2 = 90;
        next_id = 7
    }
    if(Id_fired == "page_7")
    {
        index_1 = 90;
        index_2 = 103;
        r = document.getElementById("next_page")
        r.classList.remove("active")
        r.classList.add("disabled")
    }
    if(Id_fired == "page_8")
    {
        index_1 = (next_id-1) * 15;
        index_2 = index_1+15;

        actice_class_update = document.getElementById("page_"+(next_id-1))
        actice_class_update.parentElement.classList.remove("active")

        document.getElementById("page_"+(next_id)).parentElement.classList.add("active")

        next_id+=1

        if(next_id==8)
        {
            r = document.getElementById("next_page")
            r.classList.remove("active")
            r.classList.add("disabled")
        }
    }     
    container = document.getElementById("container")
    container.innerHTML = ""   
    fetch("books.json")
            .then((res) => {
                return res.json();
            })
            .then(data =>   {
                for(let i=index_1;i<index_2;i++)
                {
                    load_books(data[i])
                }
})
}

for(let i=1;i<=8;i++)
{
    var e = "page_" + i;
    var elem = document.getElementById(e)
    index_1 = 0
    elem.addEventListener('click',load_books_by_page)
    
}
page_1 = document.getElementById("page_1")
page_1.click()