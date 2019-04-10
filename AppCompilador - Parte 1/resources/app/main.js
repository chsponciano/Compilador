const { app, BrowserWindow, dialog } = require('electron')

function createWindow () {
  	// Create the browser window.
  	let win = new BrowserWindow({ width: 900, height: 600, minWidth: 900, minHeight: 600 });

  	// and load the index.html of the app.
  	win.loadFile('index.html')
}

app.on('window-all-closed', function() {
  
  if (process.platform != 'darwin') {
    app.quit();
  }

});

app.on('ready', createWindow)
