from pydantic import BaseModel
from typing import List


class ModelLayer(BaseModel):
    layer_name: str
    input_shape: str
    output_shape: str
    params: int
    kernel_size: str


class Model(BaseModel):
    is_active: bool
    name: str
    layers: List[ModelLayer]
    total_params: int
    trainable_params: int
    non_trainable_params: int
    total_mult_adds: float
    input_size_MB: float
    forward_backward_pass_size_MB: float
    params_size_MB: float
    estimated_total_size_MB: float


class ModelShort(BaseModel):
    layers: List[str]
    input_shape: str
    output_shape: str
    total_params: int


class NetworkFlow(BaseModel):
    protocol: float
    flow_duration: float
    flow_byts_s: float
    flow_pkts_s: float
    fwd_pkts_s: float
    bwd_pkts_s: float
    tot_fwd_pkts: float
    tot_bwd_pkts: float
    totlen_fwd_pkts: float
    totlen_bwd_pkts: float
    fwd_pkt_len_max: float
    fwd_pkt_len_min: float
    fwd_pkt_len_mean: float
    fwd_pkt_len_std: float
    bwd_pkt_len_max: float
    bwd_pkt_len_min: float
    bwd_pkt_len_mean: float
    bwd_pkt_len_std: float
    pkt_len_max: float
    pkt_len_min: float
    pkt_len_mean: float
    pkt_len_std: float
    pkt_len_var: float
    fwd_header_len: float
    bwd_header_len: float
    fwd_seg_size_min: float
    fwd_act_data_pkts: float
    flow_iat_mean: float
    flow_iat_max: float
    flow_iat_min: float
    flow_iat_std: float
    fwd_iat_tot: float
    fwd_iat_max: float
    fwd_iat_min: float
    fwd_iat_mean: float
    fwd_iat_std: float
    bwd_iat_tot: float
    bwd_iat_max: float
    bwd_iat_min: float
    bwd_iat_mean: float
    bwd_iat_std: float
    fwd_psh_flags: float
    bwd_psh_flags: float
    fwd_urg_flags: float
    bwd_urg_flags: float
    fin_flag_cnt: float
    syn_flag_cnt: float
    rst_flag_cnt: float
    psh_flag_cnt: float
    ack_flag_cnt: float
    urg_flag_cnt: float
    ece_flag_cnt: float
    down_up_ratio: float
    pkt_size_avg: float
    init_fwd_win_byts: float
    init_bwd_win_byts: float
    active_max: float
    active_min: float
    active_mean: float
    active_std: float
    idle_max: float
    idle_min: float
    idle_mean: float
    idle_std: float
    fwd_byts_b_avg: float
    fwd_pkts_b_avg: float
    bwd_byts_b_avg: float
    bwd_pkts_b_avg: float
    fwd_blk_rate_avg: float
    bwd_blk_rate_avg: float
    fwd_seg_size_avg: float
    bwd_seg_size_avg: float
    cwe_flag_count: float
    subflow_fwd_pkts: float
    subflow_bwd_pkts: float
    subflow_fwd_byts: float
    subflow_bwd_byts: float


class FullNetworkFlow(NetworkFlow):
    src_ip: float
    dst_ip: float