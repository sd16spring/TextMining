clf
clear all

odyssey = csvread('odyssey_data.csv');
frankenstein = csvread('frankenstein_data.csv');
peterPan = csvread('peter_pan_data.csv');
wizard = csvread('wizard_of_oz_data.csv');
s = sum(wizard);
for i = 1:1000
    x(i) = i;
    y(i) = wizard(i);
    p(i) = s*1/(i*log(1.78*length(wizard)));
end

loglog(x, y, 'b')
hold on
loglog(x, p, 'r')
