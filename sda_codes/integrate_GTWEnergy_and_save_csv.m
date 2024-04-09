function Param1 = integrate_GTWEnergy_and_save_csv(Param)
    % Extract necessary parameters
    GTW = Param.GTW;
    Ts = Param.Ts;
    Ws = Param.Ws;

    % Define the step sizes for integration
    dt = 0.005;

    % Perform integration along both dimensions
    % integrated_GTWEnergy = trapz(Ws, trapz(Ts, GTW, 2)) * dt * dw;
    freq_Env =  trapz(Ts, GTW,2);
    time_Env =  trapz(Ws, GTW,1);



    % Add the integrated energy to the Param structure
    Param1.freq_Env = freq_Env;
    Param1.time_Env= time_Env;

    % Save the result to a CSV file
    csv_data1 = freq_Env;  % Convert to a matrix if there are more data to save
    writematrix(csv_data1,"freq_Env.csv");
      % Save the result to a CSV file
    csv_data2 = freq_Env;  % Convert to a matrix if there are more data to save
    writematrix(csv_data2,"time_Env.csv");
end


% % Example usage:
% EWa = resampledSignal
% dt = 0.005;
% Param = EPSDParam(EWa, dt);
% 
% % Integrate GTW energy and save to CSV file
% integrate_GTWEnergy_and_save_csv(Param);
% clc


