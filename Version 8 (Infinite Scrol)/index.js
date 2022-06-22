function loadBook() {
fetch("books.json")
        .then((res) => {
            return res.json();
        })
        .then(data =>   {
    const book = document.createElement("div")
    book.classList.add("book_container","col-sm-4")
    book_data = data[Math.floor(Math.random() * 99)]
    rating = Math.floor(Math.random() * 200 + 1)

    book.innerHTML =
    `
                            <img src="${book_data["imageLink"]}" alt="">
                            <p  class="book_name"><a href="${book_data["link"]}" target="_blank"> ${book_data["title"]}</br> By ${book_data["author"]}</p></a></p>
                            <div class="align-left">
                                <p class=" price green">${book_data["author"]}</p>
                                <p class="stock in_stock " data-stock="in stock"><i class="fa fa-check" aria-hidden="true"></i> In stock</p>
                                <div><span class="fa fa-star"></span><span class="fa fa-star "></span><span class="fa fa-star"></span><span class="fa fa-star "></span><span class="fa fa-star not_filled"></span></div>
                                <p class="review green" data-rating="${rating}">${rating} Reviews</p>
                                <button>Add to cart</button>
                            </div>
    `
    container = document.getElementById("container")
    container.appendChild(book)})
}

for (let i=0;i<9;i++)
{
    loadBook()
}

