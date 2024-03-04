let slideIndex = 0;

    function showSlides() {
        let slides = document.querySelectorAll('.slide-img');

        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = 'none';
        }

        slideIndex++;

        if (slideIndex > slides.length) {
            slideIndex = 1;
        }

        slides[slideIndex - 1].style.display = 'block';

        setTimeout(showSlides, 2000); // Change slide every 2 seconds
    }

    // Call the function to start the slideshow
    showSlides();
