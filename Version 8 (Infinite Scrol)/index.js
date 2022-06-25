count = 0;
const loading = document.querySelector('.loading');

function loadBook() {
fetch("books.json")
        .then((res) => {
            return res.json();
        })
        .then(data =>   {
    const book = document.createElement("div")
    book.classList.add("book_container","col-sm-4")
    book_data = data[count]
    count++;

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
    container.appendChild(book)})

    loading.classList.remove('show');
}

function load_books()
{
    if(count > 102)
    {
        showlastPage()
        window.removeEventListener('scroll', show_more)
        loading.classList.remove('show');
        return
    }
    for (let i=0;i<9;i++)
    {
        loadBook()
    }
}
load_books()

function showlastPage(){
    console.log("I got u");
    const elem = document.createElement("div")
    elem.classList.add("book_container","col-sm-12")
    elem.innerHTML = `
    <div class="card" style="width: 18rem;">
    <div class="card-header">
    Looks like you've reached the end
    </div>
    </div>
    `
    app = document.getElementById("container")
    app.appendChild(elem)
}

function showLoading() {
        loading.classList.add('show');
        setTimeout(load_books, 1000); 
}

window.addEventListener('scroll', show_more);

function show_more()
{
    const { scrollTop, scrollHeight, clientHeight } = document.documentElement;
	
	//console.log( { scrollTop, scrollHeight, clientHeight });
	if(clientHeight + scrollTop >= scrollHeight - 10) {
		showLoading();
	}
}