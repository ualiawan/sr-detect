 
# Deep Back-Projection Networks for Super-Resolution (CVPR2018)

This is a detection test code taken from following project.

Project page: https://alterzero.github.io/projects/DBPN.html

## Dependencies
* Python 3.5
* PyTorch >= 1.0.0

## Model types
1. "DBPN"
2. "DBPN-RES-MR64-3" -> [improvement of DBPN](https://arxiv.org/abs/1904.05677) with recurrent process + residual learning

##########HOW TO##########

#Testing

    ```python3
    eval.py
    ```

![DBPN](http://www.toyota-ti.ac.jp/Lab/Denshi/iim/members/muhammad.haris/projects/DBPN.png)

## Citations
This rpeo is based on follwoing works
```
@inproceedings{DBPN2018,
  title={Deep Back-Projection Networks for Super-Resolution},
  author={Haris, Muhammad and Shakhnarovich, Greg and Ukita, Norimichi},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2018}
}

@article{DBPN2019,
  title={Deep Back-Projection Networks for Single Imaage Super-Resolution},
  author={Haris, Muhammad and Shakhnarovich, Greg and Ukita, Norimichi},
  journal={arXiv preprint arXiv:1904.05677},
  year={2019}
}

```
