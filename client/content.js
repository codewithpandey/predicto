chrome.runtime.sendMessage({ todo: "showPageAction" })

window.addEventListener('DOMFocusIn', function () {

    let stars = [];
    let review = document.querySelector('textarea._3kRe7w');

    document.querySelector('._2teBVu').childNodes.forEach(child => stars.push(child));

    stars.reverse();
    stars.unshift(0);

    review.addEventListener('keyup', function (e) {

        let reviewText = e.target.value;

        if (reviewTextIncludes('awesome'))  updateRating(5);
        if (reviewTextIncludes('amazing'))  updateRating(5);
        if (reviewTextIncludes('decent'))   updateRating(3);
        if (reviewTextIncludes('worst'))    updateRating(1);
        if (reviewTextIncludes('great'))    updateRating(4);
        if (reviewTextIncludes('cool'))     updateRating(3);
        if (reviewTextIncludes('nice'))     updateRating(4);
        if (reviewTextIncludes('bad'))      updateRating(1);

        function reviewTextIncludes(word) {
            //splits the review text at the spaces, and checks if the given word exists.
            return reviewText.split(' ').includes(word) ? true : false;
        }
    });

    function updateRating(digit) {
        //early returns, fail checks.
        if(digit == undefined || digit == null) return;
        if(digit < 0 || digit > 5)   return console.error('rating not within the range 1 to 5');
        if(!Number.isInteger(digit)) return console.error(`rating must be an Integer, recieved ${typeof digit}!`)

        stars[digit].click();
    }

}, false);



