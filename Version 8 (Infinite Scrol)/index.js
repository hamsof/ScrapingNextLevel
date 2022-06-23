count = 0
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

    loading.classList.remove('show');
}

function load_books()
{
    for (let i=0;i<9;i++)
    {
        loadBook()
    }
}

window.addEventListener('scroll', () => {
	const { scrollTop, scrollHeight, clientHeight } = document.documentElement;
	
	console.log( { scrollTop, scrollHeight, clientHeight });
	
	if(clientHeight + scrollTop >= scrollHeight - 5) {
		// show the loading animation
		showLoading();
	}
});

function showLoading() {
	// load more data
    loading.classList.add('show');
    setTimeout(load_books, 1000); 
}

load_books()