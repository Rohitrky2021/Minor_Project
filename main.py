from ENHANCENET import ENHANCENET
import argparse
from utils import *

def parse_args():
    desc = "Pytorch implementation of NightImageEnhancement"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--phase', type=str, default='test', help='[train / test]')
    parser.add_argument('--dataset', type=str, default='LOL', help='dataset_name')
    parser.add_argument('--datasetpath', type=str, default='LOL', help='/home1/yeying/data/LOL_Cap/')
    parser.add_argument('--iteration', type=int, default=1000000, help='The number of training iterations')
    parser.add_argument('--batch_size', type=int, default=1, help='The size of batch size')
    parser.add_argument('--print_freq', type=int, default=1000, help='The number of image print freq')
    parser.add_argument('--save_freq', type=int, default=100000, help='The number of model save freq')
    parser.add_argument('--decay_flag', type=str2bool, default=True, help='The decay_flag')

    parser.add_argument('--lr', type=float, default=0.0001, help='The learning rate')
    parser.add_argument('--weight_decay', type=float, default=0.0001, help='The weight decay')
    parser.add_argument('--atten_weight', type=int, default=0.0001, help='Weight for Attention Loss')
    parser.add_argument('--use_decomp_loss', type=str2bool, default=False, help='use Decomposition Loss')
    parser.add_argument('--decomp_weight', type=int, default=1, help='Weight for Decomposition Loss')
    parser.add_argument('--identity_weight', type=int, default=10, help='Weight for Identity Loss')
    parser.add_argument('--adv_weight', type=int, default=1, help='Weight for GAN')
    parser.add_argument('--cycle_weight', type=int, default=10, help='Weight for Cycle')

    parser.add_argument('--ch', type=int, default=64, help='base channel number per layer')
    parser.add_argument('--n_res', type=int, default=4, help='The number of resblock')
    parser.add_argument('--n_dis', type=int, default=6, help='The number of discriminator layer')

    parser.add_argument('--img_size', type=int, default=512, help='The training size of image')
    parser.add_argument('--img_ch', type=int, default=3, help='The size of image channel')

    parser.add_argument('--result_dir', type=str, default='results', help='Directory name to save the results')
    parser.add_argument('--device', type=str, default='cuda', choices=['cpu', 'cuda'], help='Set gpu mode; [cpu, cuda]')
    parser.add_argument('--benchmark_flag', type=str2bool, default=False)
    parser.add_argument('--resume', type=str2bool, default=True)
    
    parser.add_argument('--im_suf_A', type=str, default='.png', help='The suffix of test images [.png / .jpg]')

    return check_args(parser.parse_args())

"""checking arguments"""
def check_args(args):
    check_folder(os.path.join(args.result_dir, args.dataset, 'model'))
    check_folder(os.path.join(args.result_dir, args.dataset, 'train_img'))
    try:
        assert args.epoch >= 1
    except:
        print('number of epochs must be larger than or equal to one')
    try:
        assert args.batch_size >= 1
    except:
        print('batch size must be larger than or equal to one')
    return args

"""main"""
def main():
    args = parse_args()
    if args is None:
      exit()

    gan = ENHANCENET(args)

    if args.phase == 'test' :
        gan.build_model()
        gan.test()
        print(" Test finished!")

    if args.phase == 'train' :
        gan.build_train_model()        
        gan.train()
        print(" Training finished!")

if __name__ == '__main__':
    main()