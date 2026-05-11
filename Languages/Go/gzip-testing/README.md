Just doing some quick and dirty gzip testing to see if it's worth implementing. In my initial tests it saves ~%80 of size:


```
Original: 95162
Fast: 18112 80.97%
Smallest:14899 84.34%
```

The highest compression level seems pretty pointless in my case
