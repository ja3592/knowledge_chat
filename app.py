import streamlit as st

# 页面配置
st.set_page_config(
    page_title="工艺知识问答系统",
    page_icon="🤖",
    layout="wide"
)

# 自定义CSS样式
st.markdown("""
<style>
    .small-button {
        font-size: 12px !important;
        padding: 0.25rem 0.5rem !important;
        margin: 0.1rem 0 !important;
        height: auto !important;
        min-height: 2rem !important;
    }
    
    .stButton > button {
        font-size: 13px;
        padding: 0.3rem 0.6rem;
        height: 2.5rem;
        width: 100%;
    }
    
    .level-header {
        font-size: 14px;
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: #1f77b4;
    }
    
    .iframe-container {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        overflow: hidden;
        margin-top: 1rem;
    }
    
    .back-button {
        margin-bottom: 1rem;
    }
    
    .page-header {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 初始化session state
if 'show_categories' not in st.session_state:
    st.session_state.show_categories = False
if 'selected_level1' not in st.session_state:
    st.session_state.selected_level1 = None
if 'selected_level2' not in st.session_state:
    st.session_state.selected_level2 = None
if 'selected_level3' not in st.session_state:
    st.session_state.selected_level3 = None
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'current_link' not in st.session_state:
    st.session_state.current_link = None
if 'current_title' not in st.session_state:
    st.session_state.current_title = None

# ==================== 配置区域 ====================
# 请在这里根据您的实际情况配置知识库结构和链接

# 知识库结构配置（三级结构）
KNOWLEDGE_BASE_STRUCTURE = {
    "焊接": {
        "标准": {
            "集团标准": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm",
            "团体标准": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm", 
            "美国焊接学会标准": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm"
        },
     
        "参考资料": {
            "焊接缺欠": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm",
            "焊接疲劳": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm",
            "焊接变形": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm"
        },
     
        "工艺参数": {
            "MAG": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm",
            "激光电弧复合焊": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm",
            "螺柱焊": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm"
        }
    },
    "涂装": {
        "标准": {
            "集团标准": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r",
            "团体标准": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r", 
            "I其它标准": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r"
        },
        "参考资料": {
            "资料1": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r",
            "资料2": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r",
            "资料3": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r"
        },
        "工艺参数": {
            "参数1": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r",
            "参数2": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r",
            "参数3": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r"
        }
    },
    "装配": {
        "标准": {
            "集团标准": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf",
            "团体标准": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf", 
            "其它标准": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf"
        },
      
        "参考资料": {
            "资料1": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf",
            "资料2": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf",
            "资料3": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf"
        },
      
        "工艺参数": {
            "参数1": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf",
            "参数2": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf",
            "参数3": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf"
        }
    }
}

# 二级知识库链接配置（子方向汇总）
LEVEL2_LINKS = {
    "焊接": {
        "标准": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm",
        "参考资料": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm",
        "工艺参数": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm"
    },
    "涂装": {
        "标准": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r",
        "参考资料": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r",
        "工艺参数": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r"
    },
    "装配": {
        "标准": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf",
        "参考资料": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf",
        "工艺参数": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf"
    }
}

# 一级知识库链接配置（方向汇总）
LEVEL1_LINKS = {
    "焊接": "https://share.fastgpt.in/chat/share?shareId=dddq9d2pxrwv7n9k9fi304qm",
    "涂装": "https://share.fastgpt.in/chat/share?shareId=ktyhrap97g2lxub3fmj7kg9r",
    "装配": "https://share.fastgpt.in/chat/share?shareId=ikx5tfgl22rmgwc63e3ptrwf"
}

# 直接问答链接
DIRECT_QA_LINK = "https://share.fastgpt.in/chat/share?shareId=2ntg3m52y8mi6hg48z71iqnv"

# ==================== 配置区域结束 ====================

def reset_lower_levels(level):
    """重置下级选择"""
    if level >= 2:
        st.session_state.selected_level2 = None
    if level >= 3:
        st.session_state.selected_level3 = None

def get_target_link():
    """根据当前选择获取目标链接"""
    if st.session_state.selected_level3:
        # 三级选择：返回具体的子子方向链接
        return KNOWLEDGE_BASE_STRUCTURE[st.session_state.selected_level1][st.session_state.selected_level2][st.session_state.selected_level3]
    elif st.session_state.selected_level2:
        # 二级选择：返回子方向汇总链接
        return LEVEL2_LINKS[st.session_state.selected_level1][st.session_state.selected_level2]
    elif st.session_state.selected_level1:
        # 一级选择：返回方向汇总链接
        return LEVEL1_LINKS[st.session_state.selected_level1]
    else:
        return None

def get_current_selection_title():
    """获取当前选择的标题"""
    if st.session_state.selected_level3:
        return f"{st.session_state.selected_level1} → {st.session_state.selected_level2} → {st.session_state.selected_level3}"
    elif st.session_state.selected_level2:
        return f"{st.session_state.selected_level1} → {st.session_state.selected_level2}"
    elif st.session_state.selected_level1:
        return st.session_state.selected_level1
    else:
        return "未选择"

def go_to_qa_page(link, title):
    """跳转到问答页面"""
    st.session_state.current_page = 'qa'
    st.session_state.current_link = link
    st.session_state.current_title = title
    st.rerun()

def go_back_home():
    """返回首页"""
    st.session_state.current_page = 'home'
    st.session_state.current_link = None
    st.session_state.current_title = None
    st.rerun()

def render_qa_page():
    """渲染问答页面"""
    # 页面头部
    st.markdown(f"""
    <div class="page-header">
        <h2>🤖 知识问答 - {st.session_state.current_title}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # 返回按钮和刷新按钮
    col1, col2, col3 = st.columns([1, 1, 4])
    
    with col1:
        if st.button("🏠 返回首页/重新选择知识库", type="primary", use_container_width=True):
            go_back_home()
    
    with col2:
        if st.button("🔄 刷新页面", type="secondary", use_container_width=True):
            st.rerun()
    
    # 显示当前链接信息
    st.info(f"📍 当前知识库：{st.session_state.current_title}")

    
    # 嵌入iframe
    st.markdown("### 📖 有问题尽管问！")
    
    # 创建iframe容器
    iframe_html = f"""
    <div class="iframe-container">
        <iframe 
            src="{st.session_state.current_link}" 
            width="100%" 
            height="800" 
            frameborder="0"
            style="border: none;">
            <p>您的浏览器不支持iframe。请<a href="{st.session_state.current_link}" target="_blank">点击这里</a>访问链接。</p>
        </iframe>
    </div>
    """
    
    st.markdown(iframe_html, unsafe_allow_html=True)

def render_home_page():
    """渲染首页"""
    # 页面标题
    st.title("🤖 工艺知识问答系统")
    st.markdown("---")
    
    # 提示信息
    st.info("📚 请选择本次问答参考的知识库")
    
    # 创建两列布局
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 选择知识库按钮
        if st.button("🔍 选择知识库", type="secondary", use_container_width=True):
            st.session_state.show_categories = True
            # 重置所有选择
            st.session_state.selected_level1 = None
            st.session_state.selected_level2 = None
            st.session_state.selected_level3 = None
    
    with col2:
        # 显示当前选择路径
        if st.session_state.selected_level1:
            path_parts = [st.session_state.selected_level1]
            if st.session_state.selected_level2:
                path_parts.append(st.session_state.selected_level2)
            if st.session_state.selected_level3:
                path_parts.append(st.session_state.selected_level3)
            
            st.success(f"📍 当前选择：{' → '.join(path_parts)}")
    
    # 知识库选择区域
    if st.session_state.show_categories:
        st.markdown("### 📂 知识库选择")
        
        # 创建三列布局用于三级选择
        level_cols = st.columns(3)
        
        # 第一级选择
        with level_cols[0]:
            st.markdown('<div class="level-header">第一级：方向</div>', unsafe_allow_html=True)
            for category in KNOWLEDGE_BASE_STRUCTURE.keys():
                button_type = "primary" if st.session_state.selected_level1 == category else "secondary"
                if st.button(
                    category, 
                    key=f"level1_{category}",
                    type=button_type,
                    use_container_width=True
                ):
                    if st.session_state.selected_level1 != category:
                        st.session_state.selected_level1 = category
                        reset_lower_levels(2)
                        st.rerun()
        
        # 第二级选择
        with level_cols[1]:
            if st.session_state.selected_level1:
                st.markdown('<div class="level-header">第二级：子方向</div>', unsafe_allow_html=True)
                subcategories = KNOWLEDGE_BASE_STRUCTURE[st.session_state.selected_level1]
                for subcategory in subcategories.keys():
                    button_type = "primary" if st.session_state.selected_level2 == subcategory else "secondary"
                    if st.button(
                        subcategory,
                        key=f"level2_{subcategory}",
                        type=button_type,
                        use_container_width=True
                    ):
                        if st.session_state.selected_level2 != subcategory:
                            st.session_state.selected_level2 = subcategory
                            st.session_state.selected_level3 = None  # 重置第三级选择
                            st.rerun()
                        else:
                            # 如果点击的是已选中的按钮，不做任何操作，保持第三级显示
                            pass
        
        # 第三级选择
        with level_cols[2]:
            if st.session_state.selected_level1 and st.session_state.selected_level2:
                st.markdown('<div class="level-header">第三级：子方向细化</div>', unsafe_allow_html=True)
                try:
                    sub_subcategories = KNOWLEDGE_BASE_STRUCTURE[st.session_state.selected_level1][st.session_state.selected_level2]
                    for sub_subcategory in sub_subcategories.keys():
                        button_type = "primary" if st.session_state.selected_level3 == sub_subcategory else "secondary"
                        if st.button(
                            sub_subcategory,
                            key=f"level3_{sub_subcategory}",
                            type=button_type,
                            use_container_width=True
                        ):
                            if st.session_state.selected_level3 != sub_subcategory:
                                st.session_state.selected_level3 = sub_subcategory
                                st.rerun()
                except KeyError:
                    st.warning("该子方向下暂无更细分的选项")
    
    # 分隔线
    st.markdown("---")
    
    # 问答按钮区域
    st.markdown("### 🚀 开始问答")
    
    # 创建两列用于放置按钮
    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        # 基于知识库问答按钮
        knowledge_qa_disabled = st.session_state.selected_level1 is None
        
        if st.button(
            "📖 基于知识库问答", 
            disabled=knowledge_qa_disabled,
            type="primary",
            use_container_width=True,
            key="knowledge_qa_btn"
        ):
            target_link = get_target_link()
            if target_link:
                title = get_current_selection_title()
                go_to_qa_page(target_link, title)
    
    with btn_col2:
        # 直接问答按钮
        if st.button(
            "💬 直接问答", 
            type="secondary",
            use_container_width=True,
            key="direct_qa_btn"
        ):
            go_to_qa_page(DIRECT_QA_LINK, "直接问答")
    
    # 帮助信息
    with st.expander("ℹ️ 使用说明"):
        st.markdown("""
        **使用步骤：**
        1. 点击"选择知识库"按钮开始选择
        2. 依次选择方向、子方向、子方向细化（可以在任意级别停止选择）
        3. 选择完成后，点击"基于知识库问答"进行问答
        4. 或者直接点击"直接问答"进行通用问答
        
        **选择规则：**
        - 只选择第一级：跳转到该方向的汇总知识库
        - 选择到第二级：跳转到该子方向的知识库
        - 选择到第三级：跳转到具体的子方向细化知识库
        
        **新功能：**
        - 点击问答按钮后，会在新页面中进行问答
        - 可以通过返回按钮回到首页重新选择知识库
        """)

def main():
    """主函数"""
    # 根据当前页面状态渲染不同的页面
    if st.session_state.current_page == 'qa':
        render_qa_page()
    else:
        render_home_page()

if __name__ == "__main__":
    main()