# Welcome to kusa-bot
このレポジトリでは、github actionsを用いてpushを定期実行します。

# Actions Flow
- 09:00(JST) cronジョブ起動
- pythonの実行環境構築
- pythonファイル(btc_jpy.py)実行
- サイトスクレイピング
- 取得した値段をREADME.mdに書き込み保存
- README.mdの編集差分をコミット
- push

# Everyday BTC/JPY at 09:00(JST)
<br>2022-05-28 1BTC(JPY): 3691661<br>2022-05-28 1BTC(JPY): 3691661
<br>2022-05-29 1BTC(JPY): 3688129<br>2022-05-29 1BTC(JPY): 3653905<br>2022-05-30 1BTC(JPY): 3812789<br>2022-05-31 1BTC(JPY): 4044251<br>2022-06-01 1BTC(JPY): 4096657<br>2022-06-02 1BTC(JPY): 3864097<br>2022-06-03 1BTC(JPY): 3971973<br>2022-06-04 1BTC(JPY): 3894198<br>2022-06-05 1BTC(JPY): 3887994<br>2022-06-06 1BTC(JPY): 4033669<br>2022-06-07 1BTC(JPY): 3900584<br>2022-06-08 1BTC(JPY): 4146326<br>2022-06-09 1BTC(JPY): 4045510<br>2022-06-10 1BTC(JPY): 4018344<br>2022-06-11 1BTC(JPY): 3922619<br>2022-06-12 1BTC(JPY): 3800348<br>2022-06-13 1BTC(JPY): 3470740<br>2022-06-14 1BTC(JPY): 2836243<br>2022-06-15 1BTC(JPY): 2979207<br>2022-06-16 1BTC(JPY): 3020792<br>2022-06-17 1BTC(JPY): 2785123<br>2022-06-18 1BTC(JPY): 2741033<br>2022-06-19 1BTC(JPY): 2476684<br>2022-06-20 1BTC(JPY): 2766590<br>2022-06-21 1BTC(JPY): 2773068<br>2022-06-22 1BTC(JPY): 2779292<br>2022-06-23 1BTC(JPY): 2767454<br>2022-06-24 1BTC(JPY): 2841564<br>2022-06-25 1BTC(JPY): 2863748<br>2022-06-26 1BTC(JPY): 2891340<br>2022-06-27 1BTC(JPY): 2898676<br>2022-06-28 1BTC(JPY): 2788329<br>2022-06-29 1BTC(JPY): 2768412<br>2022-06-30 1BTC(JPY): 2736045<br>2022-07-01 1BTC(JPY): 2736296<br>2022-07-02 1BTC(JPY): 2596025<br>2022-07-03 1BTC(JPY): 2593255<br>2022-07-04 1BTC(JPY): 2593231<br>2022-07-05 1BTC(JPY): 2758700<br>2022-07-06 1BTC(JPY): 2682476<br>2022-07-07 1BTC(JPY): 2769431<br>2022-07-08 1BTC(JPY): 3004320<br>2022-07-09 1BTC(JPY): 2930676<br>2022-07-10 1BTC(JPY): 2916963<br>2022-07-11 1BTC(JPY): 2812227<br>2022-07-12 1BTC(JPY): 2735144<br>2022-07-13 1BTC(JPY): 2671649<br>2022-07-14 1BTC(JPY): 2798676<br>2022-07-15 1BTC(JPY): 2848392<br>2022-07-16 1BTC(JPY): 2869769<br>2022-07-17 1BTC(JPY): 2933130<br>2022-07-18 1BTC(JPY): 2933130<br>2022-07-19 1BTC(JPY): 3055272<br>2022-07-20 1BTC(JPY): 3211324<br>2022-07-21 1BTC(JPY): 3217485<br>2022-07-22 1BTC(JPY): 3171109<br>2022-07-23 1BTC(JPY): 3106505<br>2022-07-24 1BTC(JPY): 3042565<br>2022-07-25 1BTC(JPY): 3018681<br>2022-07-26 1BTC(JPY): 2873939<br>2022-07-27 1BTC(JPY): 2906334<br>2022-07-28 1BTC(JPY): 3092511<br>2022-07-29 1BTC(JPY): 3197067<br>2022-07-30 1BTC(JPY): 3176457<br>2022-07-31 1BTC(JPY): 3171535<br>2022-08-01 1BTC(JPY): 3102684<br>2022-08-02 1BTC(JPY): 2996860<br>2022-08-03 1BTC(JPY): 3042985<br>2022-08-04 1BTC(JPY): 3102984<br>2022-08-05 1BTC(JPY): 3008193<br>2022-08-06 1BTC(JPY): 3137067<br>2022-08-07 1BTC(JPY): 3101236<br>2022-08-08 1BTC(JPY): 3141859<br>2022-08-09 1BTC(JPY): 3199076<br>2022-08-10 1BTC(JPY): 3091394<br>2022-08-11 1BTC(JPY): 3241529<br>2022-08-12 1BTC(JPY): 3180379<br>2022-08-13 1BTC(JPY): 3265829<br>2022-08-14 1BTC(JPY): 3280072<br>2022-08-15 1BTC(JPY): 3322292<br>2022-08-16 1BTC(JPY): 3215855<br>2022-08-17 1BTC(JPY): 3221888<br>2022-08-18 1BTC(JPY): 3166911<br>2022-08-19 1BTC(JPY): 3116375<br>2022-08-20 1BTC(JPY): 2914435<br>2022-08-21 1BTC(JPY): 2914435<br>2022-08-22 1BTC(JPY): 2958151<br>2022-08-23 1BTC(JPY): 2932145<br>2022-08-24 1BTC(JPY): 2902944<br>2022-08-25 1BTC(JPY): 2946649<br>2022-08-26 1BTC(JPY): 2951629<br>2022-08-27 1BTC(JPY): 2781291<br>2022-08-28 1BTC(JPY): 2768904<br>2022-08-29 1BTC(JPY): 2768904<br>2022-08-30 1BTC(JPY): 2802803<br>2022-08-31 1BTC(JPY): 2818724<br>2022-09-01 1BTC(JPY): 2807664<br>2022-09-02 1BTC(JPY): 2821094<br>2022-09-03 1BTC(JPY): 2791714<br>2022-09-04 1BTC(JPY): 2777058<br>2022-09-05 1BTC(JPY): 2772044<br>2022-09-06 1BTC(JPY): 2779869<br>2022-09-07 1BTC(JPY): 2673371<br>2022-09-08 1BTC(JPY): 2775704<br>2022-09-09 1BTC(JPY): 2788903<br>2022-09-10 1BTC(JPY): 3035121<br>2022-09-11 1BTC(JPY): 3068529<br>2022-09-12 1BTC(JPY): 3110505<br>2022-09-13 1BTC(JPY): 3171455<br>2022-09-14 1BTC(JPY): 2947035<br>2022-09-15 1BTC(JPY): 2876953<br>2022-09-16 1BTC(JPY): 2829832<br>2022-09-17 1BTC(JPY): 2845057<br>2022-09-18 1BTC(JPY): 2868208<br>2022-09-19 1BTC(JPY): 2853137<br>2022-09-20 1BTC(JPY): 2758955<br>2022-09-21 1BTC(JPY): 2758955<br>2022-09-22 1BTC(JPY): 2702959<br>2022-09-23 1BTC(JPY): 2744088<br>2022-09-27 1BTC(JPY): 2894667<br>2022-09-28 1BTC(JPY): 2699243<br>2022-09-29 1BTC(JPY): 2804248<br>2022-09-30 1BTC(JPY): 2797469<br>2022-10-01 1BTC(JPY): 2808660<br>2022-10-02 1BTC(JPY): 2795759<br>2022-10-03 1BTC(JPY): 2778836<br>2022-10-04 1BTC(JPY): 2827509<br>2022-10-05 1BTC(JPY): 2918286<br>2022-10-06 1BTC(JPY): 2952196<br>2022-10-07 1BTC(JPY): 2898194<br>2022-10-08 1BTC(JPY): 2846739<br>2022-10-09 1BTC(JPY): 2815303<br>2022-10-10 1BTC(JPY): 2831842<br>2022-10-11 1BTC(JPY): 2782052<br>2022-10-12 1BTC(JPY): 2787297<br>2022-10-13 1BTC(JPY): 2812665<br>2022-10-14 1BTC(JPY): 2921233<br>2022-10-15 1BTC(JPY): 2852737<br>2022-10-16 1BTC(JPY): 2842618<br>2022-10-17 1BTC(JPY): 2850285<br>2022-10-18 1BTC(JPY): 2902030<br>2022-10-19 1BTC(JPY): 2877996<br>2022-10-20 1BTC(JPY): 2864919<br>2022-10-21 1BTC(JPY): 2862659<br>2022-10-22 1BTC(JPY): 2817314<br>2022-10-23 1BTC(JPY): 2834514<br>2022-10-24 1BTC(JPY): 2889716<br>2022-10-25 1BTC(JPY): 2874893<br>2022-10-26 1BTC(JPY): 2987321<br>2022-10-27 1BTC(JPY): 3031220<br>2022-10-28 1BTC(JPY): 2976004<br>2022-10-29 1BTC(JPY): 3016851<br>2022-10-30 1BTC(JPY): 3063768<br>2022-10-31 1BTC(JPY): 3038747<br>2022-11-01 1BTC(JPY): 3036601<br>2022-11-02 1BTC(JPY): 3024549<br>2022-11-03 1BTC(JPY): 2993489<br>2022-11-04 1BTC(JPY): 3004757<br>2022-11-05 1BTC(JPY): 3079929<br>2022-11-06 1BTC(JPY): 3129020<br>2022-11-07 1BTC(JPY): 3088503<br>2022-11-08 1BTC(JPY): 3069558<br>2022-11-09 1BTC(JPY): 2668201<br>2022-11-10 1BTC(JPY): 2354915<br>2022-11-11 1BTC(JPY): 2452267<br>2022-11-12 1BTC(JPY): 2338188<br>2022-11-13 1BTC(JPY): 2339748<br>2022-11-14 1BTC(JPY): 2259123<br>2022-11-15 1BTC(JPY): 2321193<br>2022-11-16 1BTC(JPY): 2353003<br>2022-11-17 1BTC(JPY): 2328398<br>2022-11-18 1BTC(JPY): 2361594<br>2022-11-19 1BTC(JPY): 2332223<br>2022-11-20 1BTC(JPY): 2327454<br>2022-11-21 1BTC(JPY): 2269208<br>2022-11-22 1BTC(JPY): 2239928<br>2022-11-23 1BTC(JPY): 2284885<br>2022-11-24 1BTC(JPY): 2328655<br>2022-11-25 1BTC(JPY): 2288675<br>2022-11-26 1BTC(JPY): 2296692<br>2022-11-27 1BTC(JPY): 2293505<br>2022-11-28 1BTC(JPY): 2304404<br>2022-11-29 1BTC(JPY): 2256124<br>2022-11-30 1BTC(JPY): 2338615<br>2022-12-01 1BTC(JPY): 2320988<br>2022-12-02 1BTC(JPY): 2293933<br>2022-12-03 1BTC(JPY): 2295783<br>2022-12-04 1BTC(JPY): 2280273<br>2022-12-05 1BTC(JPY): 2316754<br>2022-12-06 1BTC(JPY): 2329262<br>2022-12-07 1BTC(JPY): 2325440<br>2022-12-08 1BTC(JPY): 2301562<br>2022-12-09 1BTC(JPY): 2350636<br>2022-12-10 1BTC(JPY): 2345066<br>2022-12-11 1BTC(JPY): 2346088<br>2022-12-12 1BTC(JPY): 2321251<br>2022-12-13 1BTC(JPY): 2365887<br>2022-12-14 1BTC(JPY): 2409797<br>2022-12-15 1BTC(JPY): 2385891<br>2022-12-16 1BTC(JPY): 2393151<br>2022-12-17 1BTC(JPY): 2286170<br>2022-12-18 1BTC(JPY): 2290597<br>2022-12-19 1BTC(JPY): 2289018<br>2022-12-20 1BTC(JPY): 2266375<br>2022-12-21 1BTC(JPY): 2221729<br>2022-12-22 1BTC(JPY): 2225824<br>2022-12-23 1BTC(JPY): 2205633<br>2022-12-24 1BTC(JPY): 2234079<br>2022-12-25 1BTC(JPY): 2237866<br>2022-12-26 1BTC(JPY): 2236790<br>2022-12-27 1BTC(JPY): 2244028<br>2022-12-28 1BTC(JPY): 2226781<br>2022-12-29 1BTC(JPY): 2218747<br>2022-12-30 1BTC(JPY): 2205513<br>2022-12-31 1BTC(JPY): 2176030<br>2023-01-01 1BTC(JPY): 2172513<br>2023-01-02 1BTC(JPY): 2168917<br>2023-01-03 1BTC(JPY): 2177580<br>2023-01-04 1BTC(JPY): 2180694<br>2023-01-05 1BTC(JPY): 2217667<br>2023-01-06 1BTC(JPY): 2247522<br>2023-01-07 1BTC(JPY): 2243367<br>2023-01-08 1BTC(JPY): 2238845<br>2023-01-09 1BTC(JPY): 2241578<br>2023-01-10 1BTC(JPY): 2263861<br>2023-01-11 1BTC(JPY): 2310852<br>2023-01-12 1BTC(JPY): 2398826<br>2023-01-13 1BTC(JPY): 2436247<br>2023-01-14 1BTC(JPY): 2674583<br>2023-01-15 1BTC(JPY): 2651398<br>2023-01-16 1BTC(JPY): 2687425<br>2023-01-17 1BTC(JPY): 2711567<br>2023-01-18 1BTC(JPY): 2732166<br>2023-01-19 1BTC(JPY): 2657647<br>2023-01-20 1BTC(JPY): 2719936<br>2023-01-21 1BTC(JPY): 2928193<br>2023-01-22 1BTC(JPY): 2955453<br>2023-01-23 1BTC(JPY): 2943252<br>2023-01-24 1BTC(JPY): 3003702<br>2023-01-25 1BTC(JPY): 2942838<br>2023-01-26 1BTC(JPY): 3005252<br>2023-01-27 1BTC(JPY): 3006690<br>2023-01-28 1BTC(JPY): 3010830<br>2023-01-29 1BTC(JPY): 3015189<br>2023-01-30 1BTC(JPY): 3089365<br>2023-01-31 1BTC(JPY): 2974138<br>2023-02-01 1BTC(JPY): 2997211<br>2023-02-02 1BTC(JPY): 3089079<br>2023-02-03 1BTC(JPY): 3036577<br>2023-02-04 1BTC(JPY): 3072000<br>2023-02-05 1BTC(JPY): 3061986<br>2023-02-06 1BTC(JPY): 3046371<br>2023-02-07 1BTC(JPY): 3029153<br>2023-02-08 1BTC(JPY): 3053701<br>2023-02-09 1BTC(JPY): 3017818<br>2023-02-10 1BTC(JPY): 2879209<br>2023-02-11 1BTC(JPY): 2848250<br>2023-02-12 1BTC(JPY): 2870739<br>2023-02-13 1BTC(JPY): 2862995<br>2023-02-14 1BTC(JPY): 2867060<br>2023-02-15 1BTC(JPY): 2936156<br>2023-02-16 1BTC(JPY): 3290035<br>2023-02-17 1BTC(JPY): 3203140<br>2023-02-18 1BTC(JPY): 3301490<br>2023-02-19 1BTC(JPY): 3313443<br>2023-02-20 1BTC(JPY): 3255202<br>2023-02-21 1BTC(JPY): 3338205<br>2023-02-22 1BTC(JPY): 3237089<br>2023-02-23 1BTC(JPY): 3261611<br>2023-02-24 1BTC(JPY): 3227703<br>2023-02-25 1BTC(JPY): 3164603<br>2023-02-26 1BTC(JPY): 3152602<br>2023-02-27 1BTC(JPY): 3210325<br>2023-02-28 1BTC(JPY): 3202544<br>2023-03-01 1BTC(JPY): 3169233<br>2023-03-02 1BTC(JPY): 3205799<br>2023-03-03 1BTC(JPY): 3053777<br>2023-03-04 1BTC(JPY): 3045124<br>2023-03-05 1BTC(JPY): 3073426<br>2023-03-06 1BTC(JPY): 3040513<br>2023-03-07 1BTC(JPY): 3058186<br>2023-03-08 1BTC(JPY): 3044188<br>2023-03-09 1BTC(JPY): 2976428<br>2023-03-10 1BTC(JPY): 2733904<br>2023-03-11 1BTC(JPY): 2691851<br>2023-03-12 1BTC(JPY): 2770026<br>2023-03-13 1BTC(JPY): 2830411<br>2023-03-14 1BTC(JPY): 3227501<br>2023-03-15 1BTC(JPY): 3346109<br>2023-03-16 1BTC(JPY): 3240465<br>2023-03-17 1BTC(JPY): 3330921<br>2023-03-18 1BTC(JPY): 3560384<br>2023-03-19 1BTC(JPY): 3560384<br>2023-03-20 1BTC(JPY): 3687181<br>2023-03-21 1BTC(JPY): 3663579<br>2023-03-22 1BTC(JPY): 3721100<br>2023-03-23 1BTC(JPY): 3596217<br>2023-03-24 1BTC(JPY): 3689906<br>2023-03-25 1BTC(JPY): 3696833<br>2023-03-26 1BTC(JPY): 3609644<br>2023-03-27 1BTC(JPY): 3663806<br>2023-03-28 1BTC(JPY): 3524549<br>2023-03-29 1BTC(JPY): 3584531<br>2023-03-30 1BTC(JPY): 3755633<br>2023-03-31 1BTC(JPY): 3767193<br>2023-04-01 1BTC(JPY): 3774096<br>2023-04-02 1BTC(JPY): 3774096<br>2023-04-03 1BTC(JPY): 3774096<br>2023-04-04 1BTC(JPY): 3677342<br>2023-04-05 1BTC(JPY): 3767360<br>2023-04-06 1BTC(JPY): 3673912<br>2023-04-07 1BTC(JPY): 3699323<br>2023-04-08 1BTC(JPY): 3687214<br>2023-04-09 1BTC(JPY): 3707678<br>2023-04-10 1BTC(JPY): 3760781<br>2023-04-11 1BTC(JPY): 3953778<br>2023-04-12 1BTC(JPY): 4040509<br>2023-04-13 1BTC(JPY): 3994478<br>2023-04-14 1BTC(JPY): 4015598<br>2023-04-15 1BTC(JPY): 4063251<br>2023-04-16 1BTC(JPY): 4049478<br>2023-04-17 1BTC(JPY): 3999565<br>2023-04-18 1BTC(JPY): 3965916<br>2023-04-19 1BTC(JPY): 4062672<br>2023-04-20 1BTC(JPY): 3898875<br>2023-04-21 1BTC(JPY): 3789589<br>2023-04-22 1BTC(JPY): 3650742<br>2023-04-23 1BTC(JPY): 3701204<br>2023-04-24 1BTC(JPY): 3735962<br>2023-04-25 1BTC(JPY): 3691643<br>2023-04-26 1BTC(JPY): 3789325<br>2023-04-27 1BTC(JPY): 3900569<br>2023-04-28 1BTC(JPY): 3957149<br>2023-04-29 1BTC(JPY): 3982383<br>2023-04-30 1BTC(JPY): 3968033<br>2023-05-01 1BTC(JPY): 4003339<br>2023-05-02 1BTC(JPY): 3854784<br>2023-05-03 1BTC(JPY): 3893375<br>2023-05-04 1BTC(JPY): 3909556<br>2023-05-05 1BTC(JPY): 3878066<br>2023-05-06 1BTC(JPY): 3998945<br>2023-05-07 1BTC(JPY): 3904278<br>2023-05-08 1BTC(JPY): 3862032<br>2023-05-09 1BTC(JPY): 3739746<br>2023-05-10 1BTC(JPY): 3750630<br>2023-05-11 1BTC(JPY): 3697663<br>2023-05-12 1BTC(JPY): 3636578<br>2023-05-13 1BTC(JPY): 3643791<br>2023-05-14 1BTC(JPY): 3627820<br>2023-05-15 1BTC(JPY): 3641686<br>2023-05-16 1BTC(JPY): 3729704<br>2023-05-17 1BTC(JPY): 3696313<br>2023-05-18 1BTC(JPY): 3761227<br>2023-05-19 1BTC(JPY): 3722452<br>2023-05-20 1BTC(JPY): 3704235<br>2023-05-21 1BTC(JPY): 3746268<br>2023-05-22 1BTC(JPY): 3669772<br>2023-05-23 1BTC(JPY): 3716941<br>2023-05-24 1BTC(JPY): 3760288<br>2023-05-25 1BTC(JPY): 3661452<br>2023-05-26 1BTC(JPY): 3677181