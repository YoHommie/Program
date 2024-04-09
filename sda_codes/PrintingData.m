function PrintingData(accel,dt)
   %for plotting the Spectral and Pseudo Spectral Parameters
   % ee - damping in % - 5 is recommended
   ee=5;
   responsespectrum(accel.', ee,dt);

   %plotting the Furier Amplitude Spectrum 
   [f,U] = FASp(dt,accel);
   figure
   plot(f,U)
   title("Furier Amplitude Spectra");
   xlabel("frequency");
   ylabel("Magnitude")

   Param= EPSDParam(accel,dt);
   freq_Env =  trapz(Param.Ts, Param.GTW,2);
   time_Env =  trapz(Param.Ws, Param.GTW,1);

   figure
   plot(Param.Ws,freq_Env)
   title("Frequency Envelope");
   xlabel("frequency");
   ylabel("Frequency Envelope");

   figure
   plot(Param.Ts,time_Env)
   title("Time Envelope");
   xlabel("Time");
   ylabel("Time Envelope");
end