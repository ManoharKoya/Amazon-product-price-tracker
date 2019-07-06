function get_link(){
    console.log("HIHIHIHIH");
    import {python} from 'python-shell'
    // var python = require("python-shell")
  

    console.log("HELLO");
    var link = document.getElementById("URL_link").value;
    document.getElementById("URL_link").value = "";

    var options = {
        args: [link]
    }

    python.PythonShell.run('C:\Users\MK\electron-quick-start\engine\scraper.py',options, function(err,results){
        if(err) throw err;
        swal(results[0]); 
    });

    // var scraper = new python('scraper.py', options)
    // scraper.on(message, function(message){
    //     swal(message);
    // })   
}