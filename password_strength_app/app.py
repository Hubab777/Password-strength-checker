# import streamlit as st

# def check_password(password):
#     score = 0
#     tips = [] #list for storing suggestions
    
#     if len(password) >= 8:
#         score += 1
#     else:
#         tips.append("8️⃣ Use at least 8 characters.")
        
#     if any(c.isupper() for c in password):
#         score += 1
#     else:
#         tips.append("🔠 Include Uppercase letter.")
        
#     if any(c.islower() for c in password):
#         score += 1
#     else:
#         tips.append("🔡 Include Lowercase letter.")
        
#     if any(c.isdigit() for c in password):
#         score += 1
#     else:
#         tips.append("🔢 Include a digit from (0-9).")
        
#     if any(c in "!@#$%^&*" for c in password):
#         score += 1
#     else:
#         tips.append("🔣 Include a special character (!@#$%^&*).")
    
#     return score, tips

# def main():
#     st.title("🔐Password Strength Meter📏")
#     password = st.text_input("Enter Password here🔑", type="password")
    
#     if password:
#         score, tips = check_password(password)
        
#         if score == 5:
#           st.success("🟢 Your password is strong! Secured one.")
#         elif score == 3 or score == 4:
#             st.warning("🟤 Your password is moderate! Re-enter improved one.")
#         else:
#             st.error("🔴 Your password is weak! Follow these steps:")
            
#         for tip in tips:
#             st.write(tip)
    
# main()


        
import streamlit as st

# --- Custom CSS Styling ---
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
        color: #339999;
    }

    .stTextInput > div > div > input {
        font-size: 18px;
        color: #000;
    }

    .stTitle {
        font-size: 36px;
        color: #339999;
    }

    .stWarning {
        font-size: 18px;
    }

    .stSuccess {
        font-size: 18px;
    }

    .stError {
        font-size: 18px;
    }

    .stMarkdown p {
        font-size: 16px;
        color: #444;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- Password Strength Logic ---
def check_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("8️⃣ Use at least 8 characters.")
        
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("🔠 Include Uppercase letter.")
        
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("🔡 Include Lowercase letter.")
        
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("🔢 Include a digit from (0-9).")
        
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        tips.append("🔣 Include a special character (!@#$%^&*).")
    
    return score, tips

# --- Streamlit App ---
def main():
    st.title("🔐Password Strength Meter📏")
    password = st.text_input("Enter Password here🔑", type="password")

    if password:
        score, tips = check_password(password)

        if score == 5:
            st.success("🟢 Your password is strong! Secured one.")
        elif score in [3, 4]:
            st.warning("🟤 Your password is moderate! Re-enter improved one.")
        else:
            st.error("🔴 Your password is weak! Follow these steps:")

        for tip in tips:
            st.write(tip)

main()

    