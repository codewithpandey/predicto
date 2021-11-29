chrome.runtime.sendMessage({ todo: "showPageAction" });

window.addEventListener('DOMFocusIn', function () {

    console.clear();

    let reviewContainer = document.querySelector('textarea._3kRe7w');
    let stars = [];

    document.querySelector('._2teBVu')
            .childNodes
            .forEach(child => stars.push(child));

    stars.reverse();
    stars.unshift(0);

    reviewContainer.addEventListener('keyup', function (e) {

        let review = e.target.value;

        if (review.includes('awesome')) updateRating(5);
        if (review.includes('amazing')) updateRating(5);
        if (review.includes('decent'))  updateRating(3);
        if (review.includes('great'))   updateRating(4);
        if (review.includes('worst'))   updateRating(1);
        if (review.includes('cool'))    updateRating(3);
        if (review.includes('nice'))    updateRating(4);
        if (review.includes('bad'))     updateRating(1);

    });

    String.prototype.includes = function (keyword) {
        return this.split(' ').includes(keyword) ? true : false;
    }

    function updateRating(digit) {
        //early returns, fail checks.
        if (digit == undefined || digit == null) return;
        if (digit < 1 || digit > 5)   return console.error('rating not within the range 1 to 5');
        if (!Number.isInteger(digit)) return console.error(`rating must be an Integer, recieved ${typeof digit}!`)

        stars[digit].click();
    }

}, false);



