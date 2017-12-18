/**
 * Created by maciej on 18.12.17.
 */


$(document).ready(function() {
    $.ajax({
        url: 'http://127.0.0.1:8000/movies/'
    }).done(function(data) {
        var ul = $("ul");
        for (var i = 0; i < data.length; i++) {
            var movieInfo = $(`
                <ul>
                    <div class="list-group-item list-group-item-action" 
                    data-id="${data[i].id}>
                        <span class="title">${data[i].title} 
                        (${data[i].year})</span>
                        <span class="description">${data[i].description}</span>
                        <ul>
                            <li>Dyrekcja: ${data[i].director}</li>
                            <li>Obsada: ${data[i].cast}</li>
                        </ul>
                    </div>
                </ul>
            `);
            ul.append(movieInfo);
        }
    });
});