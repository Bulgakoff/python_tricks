import moda
from folder_b import mod_b
import mod_c

print(f'переменная foo из модуля А ------> {moda.foo}')
moda.bar()
print(f'переменная ------>foo  из модуля B ------> {mod_b.foo}')
mod_b.bar()
# ?////////////////////
print(f'переменная foo из модуля C ------> {mod_c.foo}')