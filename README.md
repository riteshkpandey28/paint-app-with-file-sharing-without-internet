# paint-app-with-file-sharing-without-internet

Through this application, you can paint images in your phone and share the same to the server computer/laptop 
without internet or without using any third-party file sharing application.
The user scans a qr-code from his/her phone which opens an link in web browser where the user can paint the 2 images provided and save/share the same.
All you need is for the phone and computer to be connected to a common network. 

-- STEPS TO USE THIS APP -- 
1. Download the source Code

2. Install all the packages mentioned in requirements.txt file 
    You can run the following command in command prompt/terminal 
    pip install -r requirements.txt
    
3. Connect Your phone and computer to a comman network and obtain the ip address of the network by running the following command:
    For windows, in command prompt run: ipconfig
    For Linux, in terminal run: ifconfig
    
4. Once you obtain the ip address, copy it and paste it in the following 2 places:
    (i) In qrcode folder, there is one file called qrcode.html 
        at line 30, paste the ip address in the "text" field.
        for eg, text: "ip address"
        This will create the qrcode which upon scanning will lead to the paint application.
        You can save the image of the qrcode generator for the future use.
    (ii) In app.py file, at line 88, replace the value of host with your ip address. 
         for eg, host = "ip address"
         This will run our paint application on the specified ip address.
         
5. Start the server using the command "python app.py"

6. Scan the qrcode from your phone and have fun painting the fishes. 

