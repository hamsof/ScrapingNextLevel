
var previous_elem;

function load_books_index(index_1,index_2,elem) {
if(index_1 !== 0)
{
    previous_elem.classList.remove('active')
}
previous_elem = elem
elem.classList.add("active")

fetch("books.json")
        .then((res) => {
            return res.json();
        })
        .then(data =>   {
            for(let i=index_1; i<index_2;i++)
            {
                load_books(data[i])
            }
        })
}

function load_books(index){
    const book = document.createElement("div")
    book.classList.add("book_container","col-sm-4")
    book_data = index
    rating = Math.floor(Math.random() * 200 + 1)
    price = Math.floor(Math.random() * 7000 + 3000)

    book.innerHTML =
    `
                <img src="${book_data["imageLink"]}" alt="">
                <p  class="book_name"><a href="${book_data["link"]}" target="_blank"> ${book_data["title"]}</br> By ${book_data["author"]}</p></a></p>
                <div class="align-left">
                    <p class=" price green">Rs.${price}</p>
                    <p class="stock in_stock " data-stock="in stock"><i class="fa fa-check" aria-hidden="true"></i> In stock</p>
                    <div><span class="fa fa-star"></span><span class="fa fa-star "></span><span class="fa fa-star"></span><span class="fa fa-star "></span><span class="fa fa-star not_filled"></span></div>
                    <p class="review green" data-rating="${rating}">${rating} Reviews</p>
                    <button>Add to cart</button>
                </div>
    `
    container = document.getElementById("container")
    container.innerHTML = ""
    container.appendChild(book)
}

// .addEventListener("click", load_books_index(0,15));

for(let i=1;i<=7;i++)
{
    var e = "page_" + i;
    var elem = document.getElementById(e)
    index_1 = 0
    elem.addEventListener('click',/*load_books_index(index_1,15+index_1,elem)*/
        (index_1,index_2,elem) =>{
            if(index_1 !== 0)
            {
                previous_elem.classList.remove('active')
            }
            previous_elem = elem
            elem.classList.add("active")
            
            fetch("books.json")
                    .then((res) => {
                        return res.json();
                    })
                    .then(data =>   {
                        for(let i=index_1; i<index_2;i++)
                        {
                            load_books(data[i])
                        }
        })
})
}
