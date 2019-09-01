package com.craigmsirota.lockdown;

import android.Manifest;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.lang.Math;

public class lockdown extends AppCompatActivity {

    private Button b;
    private EditText pass, ip;
    private LocationManager mLocationManager;
    private LocationListener mLocationListener;
    private String coord;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lockdown);
        b = (Button) findViewById(R.id.send);
        pass = (EditText) findViewById(R.id.pass);
        ip = (EditText) findViewById(R.id.ip);
        coord = "";

        mLocationManager = (LocationManager) getSystemService(LOCATION_SERVICE);
        mLocationListener = new LocationListener() {
            @Override
            public void onLocationChanged(Location location) {
                ((TextView) findViewById(R.id.textView3)).setText(location.getLongitude() + "/" + location.getLatitude());
                setCoord(location.getLongitude() + "/" + location.getLatitude());
            }

            @Override
            public void onStatusChanged(String s, int i, Bundle bundle) {

            }

            @Override
            public void onProviderEnabled(String s) {

            }

            @Override
            public void onProviderDisabled(String s) {

            }
        };
        if (ActivityCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // TODO: Consider calling
            //    ActivityCompat#requestPermissions
            // here to request the missing permissions, and then overriding
            //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
            //                                          int[] grantResults)
            // to handle the case where the user grants the permission. See the documentation
            // for ActivityCompat#requestPermissions for more details.
            return;
        }
        mLocationManager.requestLocationUpdates("gps", 500, 0, mLocationListener);

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                send(ip.getText().toString(), pass.getText().toString(),coord);


            }
        });
        send("127.0.0.1","test","45/45");
    }

    public void tv(String msg) {((TextView) findViewById(R.id.textView6)).setText(msg);}
    public void setCoord(String c) {
        coord = c;
    }
    private String msg = "";
    public void m(String c) {
        msg = c;
    }

    private boolean send(final String priv_ip, final String passw, final String coord) {
        Runnable myRunnable =
                new Runnable(){
                    public void run(){
                        DatagramSocket datagramSocket = null;

                        try {
                            datagramSocket = new DatagramSocket();
                            double d = (Math.random() * 100000);
                            d = ((int) d) / ((double) 1000);
                            System.out.println(d);
                            int k = (int) d;

                            String pw = "";
                            for (int i = 0; i < passw.length(); i++) {
                                pw = pw + (char)(((int) passw.charAt(i)) ^ k);
                            }
                            String msg = pw + '/' + coord + '/' + d;
                            String len = msg.length() +"";
                            if (len.length() == 1)
                                len = "00" + len;
                            else if (len.length() == 2)
                                len = "0" + len;
                            byte[] b = (len).getBytes();
                            InetAddress inetAddress = InetAddress.getByName(priv_ip);           //IP Address of python.cs.rutgers.edu  -- currently only works on pythoncsrutgerseduIP -- trying to figure out local IP
                            int inet = Log.d("InetAddr", inetAddress.toString());
                            DatagramPacket datagramPacket = new DatagramPacket(b,b.length,inetAddress,17388);

                            datagramSocket.send(datagramPacket);
                            b = (msg).getBytes();
                            datagramPacket = new DatagramPacket(b,b.length,inetAddress,17388);

                            datagramSocket.send(datagramPacket);
                            m(msg);
                            Log.d("MSG","SENT");
                        } catch (IOException e) {

                            Log.d("ERR","BEEP");
                            e.printStackTrace();
                        }
                    }
                };

        Thread thread = new Thread(myRunnable);
        thread.start();
        while(msg == ""){}
        tv(msg);
        return true;
    }

}
