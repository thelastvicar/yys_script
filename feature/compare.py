import cv2
import numpy as np

def CompareImages(large_img,  template, threshold=0.9, min_scale=0.5, max_scale=1.1, scale_step=5):
    if large_img is None or template is None:
        raise ValueError("One of the images could not be loaded.")

    # 获取原图和模板尺寸
    large_h, large_w = large_img.shape[:2]
    template_h, template_w = template.shape[:2]
    
    all_matches = []
    
    # 生成缩放比例（从 min_scale 到 max_scale 的均匀分布）
    scales = np.linspace(min_scale, max_scale, scale_step)
    
    for scale in scales:
        # 计算缩放后的模板尺寸
        scaled_w = int(template_w * scale)
        scaled_h = int(template_h * scale)
        
        # 跳过尺寸超过原图的模板
        if scaled_w > large_w or scaled_h > large_h:
            continue
        
        # 缩放模板
        scaled_template = cv2.resize(
            template, 
            (scaled_w, scaled_h), 
            interpolation=cv2.INTER_AREA  # 缩放插值方法
        )
        
        # 执行模板匹配（使用归一化相关系数算法）
        result = cv2.matchTemplate(
            large_img, 
            scaled_template, 
            cv2.TM_CCOEFF_NORMED
        )
        
        # 找到所有超过阈值的匹配位置
        locations = np.where(result >= threshold)
        
        # 记录匹配区域（左上角、右下角坐标 + 缩放比例）
        for pt in zip(*locations[::-1]):  # (x, y) 顺序
            x1, y1 = pt
            x2, y2 = x1 + scaled_w, y1 + scaled_h
            all_matches.append((x1, y1, x2, y2, scale))
    
    # 去除重复或高度重叠的匹配区域
    unique_matches = remove_overlapping_matches(all_matches, overlap_threshold=0.5)
    return unique_matches

def remove_overlapping_matches(matches, overlap_threshold=0.5):
    """
    去除重叠度过高的匹配区域
    :param overlap_threshold: 重叠面积阈值（超过此值视为重复）
    """
    if not matches:
        return []
    
    # 按匹配区域面积排序（保留较大的区域）
    matches.sort(key=lambda m: (m[2]-m[0])*(m[3]-m[1]), reverse=True)
    unique = []
    
    for match in matches:
        x1, y1, x2, y2, scale = match
        # 计算当前区域面积
        area = (x2 - x1) * (y2 - y1)
        keep = True
        
        # 与已保留的区域比较重叠度
        for u in unique:
            u_x1, u_y1, u_x2, u_y2, _ = u
            # 计算交集区域
            inter_x1 = max(x1, u_x1)
            inter_y1 = max(y1, u_y1)
            inter_x2 = min(x2, u_x2)
            inter_y2 = min(y2, u_y2)
            
            inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)
            overlap = inter_area / area  # 重叠比例
            
            if overlap > overlap_threshold:
                keep = False
                break
        
        if keep:
            unique.append(match)
    
    return unique